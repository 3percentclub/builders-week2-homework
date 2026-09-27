# Builders Week 2 Homework: Fix the Date Bug

**Time:** 15–20 minutes. **You need:** a browser and a GitHub account. Nothing to install.

Our event bot reads a show notice and puts the event on the calendar. It has a bug: it grabs the **first** date it sees. In this notice, that's the presale RSVP lottery, so 500 ticket-holders show up to an empty Bushwick warehouse a week early.

> BK UNDERGROUND SESSIONS #12: Presale RSVP lottery drops **October 14, 2026** at 6:00 PM online. Secret warehouse doors open **October 21, 2026** at 11:00 PM for the live set. Curfew strictly midnight. 21+ only.

It's the same trap as the in-class lab: code that runs without errors can still give you the wrong answer.

## Steps

1. Click **Use this template** → **Create a new repository**. Make it public.
2. In your new repo, click **Code** → **Codespaces** → **Create codespace on main**.
3. In the terminal, run:
   ```
   python -m unittest -v
   ```
   2 of the 4 tests fail. That's expected.
4. Open `extractor.py` and fix `extract_event_date()`. Only edit that file.
5. Run the tests again until all 4 pass.
6. Commit and push. In Codespaces: open **Source Control** (left sidebar), type a message, click **Commit**, then **Sync Changes**.
7. Open the **Actions** tab in your repo and confirm the green checkmark.

## Rules for the fix

- The tests use **different notices** on purpose. Hard-coding `"2026-10-21"` or always taking the second date will fail.
- Your code has to work out what each date is **for**. Hint: a date next to words like *RSVP*, *presale*, *by*, *closes*, or *deadline* is not the event.
- If there's no event date, return `None`. Don't guess.
- You can use AI to help. You should still be able to explain your fix in one sentence.

## Stuck?

Post in Discord **#builders** with the error message you see.
