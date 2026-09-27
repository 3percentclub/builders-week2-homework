"""Bonus for students with an API key: light model first, heavy model only when needed.

Works with DeepSeek by default, or with any OpenAI-compatible provider (OpenRouter, Ollama, etc.).
Standard library only, so there's nothing to install.

    export LLM_API_KEY=your-key
    python escalate.py

Optional settings (defaults are for DeepSeek):
    LLM_BASE_URL   https://api.deepseek.com
    LIGHT_MODEL    deepseek-flash
    HEAVY_MODEL    deepseek-v4-pro
"""

import json
import os
import sys
import urllib.error
import urllib.request

from extractor import NOTICE
from router import INBOX, route

BASE_URL = os.environ.get("LLM_BASE_URL", "https://api.deepseek.com").rstrip("/")
LIGHT_MODEL = os.environ.get("LIGHT_MODEL", "deepseek-flash")
HEAVY_MODEL = os.environ.get("HEAVY_MODEL", "deepseek-v4-pro")

SYSTEM_PROMPT = (
    "You answer questions for an event bot. Use only this notice:\n"
    f"{NOTICE}\n"
    "Reply in two sentences or fewer. "
    "If you are not confident, or the question needs judgment, reply with exactly: ESCALATE"
)


def ask(model, message):
    """Send one chat request. Return (reply_text, total_tokens)."""
    body = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message},
        ],
        "max_tokens": 300,
    }).encode()
    request = urllib.request.Request(
        f"{BASE_URL}/chat/completions",
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ.get('LLM_API_KEY', '')}",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            data = json.load(response)
    except urllib.error.HTTPError as error:
        sys.exit(f"API error {error.code} from {model}: {error.read().decode()[:300]}\n"
                 "401 = check your key. 402 = add balance. 404 = check the model name.")
    except urllib.error.URLError as error:
        sys.exit(f"Could not reach {BASE_URL}: {error.reason}")
    reply = (data["choices"][0]["message"].get("content") or "").strip()
    tokens = data.get("usage", {}).get("total_tokens", 0)
    return reply, tokens


def handle(message):
    """Route one message. Return (who_answered, reply, tokens)."""
    tier = route(message)
    if tier == "rules":
        return "code", "(answered by code from the notice)", 0
    if tier == "human":
        return "human", "(sent to a person, no model call)", 0
    reply, tokens = ask(LIGHT_MODEL, message)
    if reply.upper().startswith("ESCALATE"):
        reply, heavy_tokens = ask(HEAVY_MODEL, message)
        return HEAVY_MODEL, reply, tokens + heavy_tokens
    return LIGHT_MODEL, reply, tokens


if __name__ == "__main__":
    if not os.environ.get("LLM_API_KEY"):
        sys.exit("Set LLM_API_KEY first. No key? Do the router challenge instead, no key needed.")
    totals = {}
    for message in INBOX:
        who, reply, tokens = handle(message)
        totals[who] = totals.get(who, 0) + tokens
        print(f"[{who}, {tokens} tokens] {message}\n    {reply}\n")
    print("Tokens by who answered:", totals)
