import unittest

from extractor import NOTICE, extract_event_date


class TestExtractEventDate(unittest.TestCase):
    def test_1_skips_the_rsvp_deadline(self):
        self.assertEqual(extract_event_date(NOTICE), "2026-10-21")

    def test_2_works_when_the_event_date_comes_first(self):
        notice = (
            "Neighborhood Tech Help Night is on November 5, 2026 at 7:00 PM. "
            "Please RSVP by November 1, 2026."
        )
        self.assertEqual(extract_event_date(notice), "2026-11-05")

    def test_3_returns_none_when_only_a_deadline_is_given(self):
        notice = (
            "Registration for the Spring Coding Circle closes March 2, 2027. "
            "Event date to be announced."
        )
        self.assertIsNone(extract_event_date(notice))

    def test_4_single_event_date_still_works(self):
        notice = "Join us on December 3, 2026 for Community Demo Night."
        self.assertEqual(extract_event_date(notice), "2026-12-03")


if __name__ == "__main__":
    unittest.main()
