import unittest

from auth import authenticate


class AuthenticationTests(unittest.TestCase):
    def test_valid_credentials_are_accepted(self):
        self.assertTrue(authenticate("demo", "correct-horse"))

    def test_wrong_password_is_rejected(self):
        self.assertFalse(authenticate("demo", "wrong-password"))


if __name__ == "__main__":
    unittest.main()
