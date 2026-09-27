"""Week 2 homework: fix the date extractor.

Our event bot reads community notices and puts the EVENT date on the calendar.
Right now it grabs the first date it sees, which is often the RSVP deadline.

Your job: change extract_event_date() so it returns the date of the event itself.
Only edit this file. Run the tests with:  python -m unittest -v
"""

import re
from datetime import datetime

NOTICE = (
    "Community AI Workshop at the Brooklyn Public Library. "
    "RSVP by October 14, 2026 to save your seat. "
    "The workshop is on October 21, 2026 at 6:00 PM in the main hall. "
    "Join in person or on Zoom."
)

DATE_PATTERN = r"(January|February|March|April|May|June|July|August|September|October|November|December) (\d{1,2}), (\d{4})"


def to_iso(match):
    """Turn a regex match like 'October 21, 2026' into '2026-10-21'."""
    return datetime.strptime(match.group(0), "%B %d, %Y").strftime("%Y-%m-%d")


def extract_event_date(text):
    """Return the event date as 'YYYY-MM-DD', or None if the notice has no event date.

    BUG: this returns the first date in the text, even when that date is a deadline.
    """
    match = re.search(DATE_PATTERN, text)
    if match:
        return to_iso(match)
    return None


if __name__ == "__main__":
    print("Event date:", extract_event_date(NOTICE))
