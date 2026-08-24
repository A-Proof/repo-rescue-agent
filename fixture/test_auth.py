import unittest

from auth import authenticate


class AuthenticationTests(unittest.TestCase):
    def test_valid_credentials_are_accepted(self):
        self.assertTrue(authenticate("demo", "correct-horse"))

    def test_wrong_password_is_rejected(self):
        self.assertFalse(authenticate("demo", "wrong-password"))

    def test_wrong_username_is_rejected(self):
        self.assertFalse(authenticate("other-user", "correct-horse"))

    def test_password_equal_to_username_is_rejected(self):
        self.assertFalse(authenticate("demo", "demo"))


if __name__ == "__main__":
    unittest.main()
