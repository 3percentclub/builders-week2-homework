import unittest

import router

RULES = [
    "What time do doors open?",
    "Is this 21+?",
    "When is curfew?",
    "What date is the show?",
    "Is there an age limit?",
    "what time does it end",
]

MODEL = [
    "What's the vibe, more techno or house?",
    "Write a hype caption for my group chat",
    "What should I wear to a warehouse party?",
    "Can you describe the event for my friend?",
]

HUMAN = [
    "I got hurt near the doors and need help",
    "I was charged twice for my ticket",
    "I lost my ID, can you let me in anyway?",
    "Can I get a refund if I miss curfew?",
    "Someone is harassing people outside the doors",
    "My friend is 20, can you make an exception?",
]


@unittest.skipUnless(router.ATTEMPTING, "Optional challenge: set ATTEMPTING = True in router.py")
class TestRouter(unittest.TestCase):
    def check(self, messages, expected):
        for message in messages:
            with self.subTest(message=message):
                self.assertEqual(router.route(message), expected)

    def test_1_plain_facts_go_to_rules(self):
        self.check(RULES, "rules")

    def test_2_language_tasks_go_to_a_model(self):
        self.check(MODEL, "model")

    def test_3_money_safety_and_exceptions_go_to_a_human(self):
        self.check(HUMAN, "human")


if __name__ == "__main__":
    unittest.main()
