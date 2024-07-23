import unittest

class TestUser(unittest.TestCase):

    def test_user_creation(self):
        user = User(email="test@example.com", first_name="Kamilo", last_name="Rubio")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.first_name, "Kamilo")
        self.assertEqual(user.last_name, "Rubio")
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

    def test_unique_email(self):
        user1 = User(email="unique@example.com", first_name="Jane", last_name="Campbell")
        with self.assertRaises(ValueError):
            user2 = User(email="unique@example.com", first_name="Jake", last_name="Tristan")

if __name__ == '__main__':
    unittest.main()