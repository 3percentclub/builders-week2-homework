# Decision: The Three C's

One or two sentences each. Replace the text after each arrow.

## Level 1 (required)

**Complexity:** Is this job deterministic (rules can do it), semantic (needs to understand meaning), or a judgment call? Did you route it to code or a model, and why?
→

**Context:** What did your code need to know to tell the presale date apart from the show date?
→

**Criticism:** What would a basic test like `assert len(date) > 0` miss? What should a human still check before the event goes on the calendar?
→

## Level 2 (optional challenge)

**Order matters:** Why does the human check have to run before the rules check?
→

**Cost:** `python router.py` prints how many messages still reach an LLM. What was it before and after your changes?
→

**Your call:** Pick one message you could argue belongs in a different tier. Where did you put it, and why?
→

## Level 3 (optional bonus)

**Escalation:** Which messages escalated to the heavy model? Was the heavy answer worth the extra tokens?
→

**One change:** What did you change (prompt, escalation rule, or model), and what happened to the token totals?
→
