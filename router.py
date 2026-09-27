"""Optional challenge: route the event bot's inbox. No API key needed.

The BK UNDERGROUND SESSIONS #12 inbox is filling up. Right now every message
goes to an LLM, which is the slow, expensive default. Route each message to the
smallest tier that can handle it safely:

    "rules"  - a plain fact from the notice (doors, date, curfew, age). Code can answer. Cost: $0.
    "model"  - needs language skills (vibe, captions, advice). A light model can draft it.
    "human"  - money, safety, or exceptions to policy. A person must decide.

Step 1: change ATTEMPTING to True so the challenge tests run.
Step 2: rewrite route() until all router tests pass.
See the report any time with:  python router.py
"""

ATTEMPTING = False

INBOX = [
    "What time do doors open?",
    "Is this 21+?",
    "When is curfew?",
    "What's the vibe, more techno or house?",
    "Write a hype caption for my group chat",
    "I got hurt near the doors and need help",
    "I was charged twice for my ticket",
    "I lost my ID, can you let me in anyway?",
]


def route(message):
    """Return "rules", "model", or "human" for one inbox message."""
    return "model"


if __name__ == "__main__":
    counts = {"rules": 0, "model": 0, "human": 0}
    for message in INBOX:
        tier = route(message)
        counts[tier] = counts.get(tier, 0) + 1
        print(f"{tier:>6}  {message}")
    print(f"\nLLM calls: {counts['model']} of {len(INBOX)} messages")
