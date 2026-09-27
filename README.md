# Builders Week 2 Homework: Fix the Date Bug

**Time:** 15–20 minutes. **You need:** a free GitHub account and a browser. Nothing to install and nothing to pay for.

Our event bot reads a show notice and puts the event on the calendar. It has a bug: it grabs the **first** date it sees. In this notice, that's the presale RSVP lottery, so 500 ticket-holders show up to an empty Bushwick warehouse a week early.

> BK UNDERGROUND SESSIONS #12: Presale RSVP lottery drops **October 14, 2026** at 6:00 PM online. Secret warehouse doors open **October 21, 2026** at 11:00 PM for the live set. Curfew strictly midnight. 21+ only.

It's the same trap as the in-class lab: code that runs without errors can still give you the wrong answer.

## Steps (all on github.com)

1. Click **Use this template** → **Create a new repository**. Make it public.
2. Wait about a minute, then open the **Actions** tab. You'll see a red X. That's expected: 2 of the 4 tests fail. Click into the run to see which ones.
3. Open `extractor.py`, click the **pencil icon** to edit, and fix `extract_event_date()`. Click **Commit changes**.
4. Go back to **Actions**. The tests run again automatically. If you see a red X, click into it, read the failure, and edit again.
5. Keep going until you get a **green checkmark**.
6. Open `decision.md`, click the pencil, and answer the Three C's questions. Commit.

## Rules for the fix

- The tests use **different notices** on purpose. Hard-coding `"2026-10-21"` or always taking the second date will fail.
- Your code has to work out what each date is **for**. Hint: a date next to words like *RSVP*, *presale*, *by*, *closes*, or *deadline* is not the event.
- If there's no event date, return `None`. Don't guess.
- You can use AI to help. You should still be able to explain your fix in one sentence.

## Optional: run the tests on your own computer

If you have Python 3 installed, clone your repo and run `python -m unittest -v`. Codespaces also works if you prefer it, but you don't need it.

## Stuck?

Post in Discord **#builders** with a screenshot of the red X in Actions.
