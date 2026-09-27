"""Bonus for students with an API key: light model first, heavy model only when needed.

Bring any provider with an OpenAI-compatible chat endpoint (most of them have one).
Standard library only, so there's nothing to install. Set these four values:

    LLM_API_KEY    your key
    LLM_BASE_URL   your provider's OpenAI-compatible base URL (see README)
    LIGHT_MODEL    a cheap, fast model from that provider
    HEAVY_MODEL    a stronger model from that provider

    python escalate.py
"""

import json
import os
import sys
import urllib.error
import urllib.request

from extractor import NOTICE
from router import INBOX, route

REQUIRED = ["LLM_API_KEY", "LLM_BASE_URL", "LIGHT_MODEL", "HEAVY_MODEL"]

SYSTEM_PROMPT = (
    "You answer questions for an event bot. Use only this notice:\n"
    f"{NOTICE}\n"
    "Reply in two sentences or fewer. "
    "If you are not confident, or the question needs judgment, reply with exactly: ESCALATE"
)


def ask(model, message):
    """Send one chat request. Return (reply_text, total_tokens)."""
    base_url = os.environ["LLM_BASE_URL"].rstrip("/")
    body = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message},
        ],
    }).encode()
    request = urllib.request.Request(
        f"{base_url}/chat/completions",
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ['LLM_API_KEY']}",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            data = json.load(response)
    except urllib.error.HTTPError as error:
        sys.exit(f"API error {error.code} from {model}: {error.read().decode()[:300]}\n"
                 "401/403 = check your key. 402/429 = add credit or wait. "
                 "404 = check LLM_BASE_URL and the model name.")
    except urllib.error.URLError as error:
        sys.exit(f"Could not reach {base_url}: {error.reason}")
    reply = (data["choices"][0]["message"].get("content") or "").strip()
    tokens = (data.get("usage") or {}).get("total_tokens", 0)
    return reply, tokens


def handle(message, light, heavy):
    """Route one message. Return (who_answered, reply, tokens)."""
    tier = route(message)
    if tier == "rules":
        return "code", "(answered by code from the notice)", 0
    if tier == "human":
        return "human", "(sent to a person, no model call)", 0
    reply, tokens = ask(light, message)
    if reply.upper().startswith("ESCALATE"):
        reply, heavy_tokens = ask(heavy, message)
        return heavy, reply, tokens + heavy_tokens
    return light, reply, tokens


if __name__ == "__main__":
    missing = [name for name in REQUIRED if not os.environ.get(name)]
    if missing:
        sys.exit(f"Missing: {', '.join(missing)}. See Level 3 in the README.\n"
                 "No key? Do the Level 2 router challenge instead, no key needed.")
    light, heavy = os.environ["LIGHT_MODEL"], os.environ["HEAVY_MODEL"]
    totals = {}
    for message in INBOX:
        who, reply, tokens = handle(message, light, heavy)
        totals[who] = totals.get(who, 0) + tokens
        print(f"[{who}, {tokens} tokens] {message}\n    {reply}\n")
    print("Tokens by who answered:", totals)
