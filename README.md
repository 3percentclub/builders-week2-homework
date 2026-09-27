# Builders Week 2 Homework: Route It Right

**You need:** a free GitHub account and a browser. Nothing to install and nothing to pay for.

This week's rule: **choose the smallest thing likely to succeed, test it, and only escalate when you know why.** This homework lets you practice that at three levels. Everyone does Level 1. Levels 2 and 3 are optional.

| Level | What you do | Time | API key? |
|---|---|---|---|
| **1. Required** | Fix the date bug + answer the Three C's | 15–20 min | No |
| **2. Challenge** | Route the event bot's inbox: rules, model, or human | 20–30 min | No |
| **3. Bonus** | Send model-tier messages to a light model, escalate to a heavy one, compare tokens | 20–30 min | Yes (DeepSeek or any OpenAI-compatible provider) |

## Setup (all on github.com)

1. Click **Use this template** → **Create a new repository**. Make it public.
2. Wait about a minute, then open the **Actions** tab. You'll see a red X. That's expected: 2 tests fail. Click into the run to see which ones.
3. To edit any file, open it and click the **pencil icon**, then **Commit changes**. The tests re-run automatically in **Actions**.

## Level 1 (required): Fix the date bug

Our event bot reads a show notice and puts the event on the calendar. It grabs the **first** date it sees. In this notice, that's the presale lottery, so 500 ticket-holders show up to an empty Bushwick warehouse a week early.

> BK UNDERGROUND SESSIONS #12: Presale RSVP lottery drops **October 14, 2026** at 6:00 PM online. Secret warehouse doors open **October 21, 2026** at 11:00 PM for the live set. Curfew strictly midnight. 21+ only.

It's the same trap as the rezoning notice in class: code that runs without errors can still give you the wrong answer.

1. In `extractor.py`, fix `extract_event_date()` so it returns the show date.
2. Keep committing until **Actions** shows a green checkmark.
3. Answer the Three C's questions in `decision.md`.

**Rules:** The tests use different notices on purpose, so hard-coding `"2026-10-21"` or always taking the second date will fail. Your code has to work out what each date is **for**. Hint: a date near *RSVP*, *presale*, *by*, *closes*, or *deadline* isn't the event. If there's no event date, return `None`. You can use AI, but you should be able to explain your fix in one sentence.

## Level 2 (challenge, no key): Route the inbox

Right now `router.py` sends **every** message to an LLM. That's the expensive default. Route each message to the smallest tier that can handle it safely:

- **rules**: a plain fact from the notice (doors, date, curfew, age). Code answers it for $0.
- **model**: needs language skills (vibe, captions, advice). A light model drafts it.
- **human**: money, safety, or exceptions to policy. A person decides.

1. In `router.py`, change `ATTEMPTING = False` to `ATTEMPTING = True`. The router tests will start running (and failing).
2. Rewrite `route()` until all tests pass. Keywords and `if` statements are enough.
3. Answer the challenge questions at the bottom of `decision.md`.

Watch for traps: *"I got hurt near the doors"* mentions doors, but it isn't a question about door times. And *"friend"* contains *"end"*. Don't just paste the test sentences into your code; write rules that would work on messages you haven't seen.

## Level 3 (bonus, API key): Light first, heavy only when needed

`escalate.py` takes your router from Level 2 and sends only the **model**-tier messages to an LLM. It tries a light model first. If the light model replies `ESCALATE`, it retries with a heavy model. Then it prints the tokens each tier used. Rules and human messages cost 0 tokens.

Defaults are DeepSeek (`deepseek-flash` → `deepseek-v4-pro`). It uses Python's standard library only, so there's nothing to install.

**Run it in Google Colab (no terminal needed):** add your key under **Secrets** (key icon on the left) as `LLM_API_KEY`, then run:

```python
!git clone https://github.com/YOUR-USERNAME/YOUR-REPO
%cd YOUR-REPO
import os
from google.colab import userdata
os.environ["LLM_API_KEY"] = userdata.get("LLM_API_KEY")
!python escalate.py
```

**Or on your own computer:** `export LLM_API_KEY=your-key` then `python escalate.py`.

**Other providers:** set `LLM_BASE_URL`, `LIGHT_MODEL`, and `HEAVY_MODEL` to any OpenAI-compatible endpoint and model IDs (OpenRouter, a local Ollama at `http://localhost:11434/v1`, etc.).

Then try one change and see what it does to cost: edit the system prompt, change what counts as `ESCALATE`, or swap the light model. Answer the bonus questions in `decision.md`. **Never commit your API key.**

## What to submit (Google Classroom)

A link to your repo with a green checkmark in **Actions**. If you did Level 2 or 3, say so in your submission.

## Stuck?

Post in Discord **#builders** with a screenshot of the red X in Actions.
