import unittest

class TestReview(unittest.TestCase):

    def test_review_creation(self):
        user = User(email="reviewer@example.com", first_name="Kamilo", last_name="Rubio")
        place = Place(name="Atmopel Place", host=user, latitude=10.0, longitude=20.0, price_per_night=80, max_guests=2)
        review = Review(place=place, user=user, text="Great place!")
        self.assertEqual(review.place, place)
        self.assertEqual(review.user, user)
        self.assertEqual(review.text, "Great place!")
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)

if __name__ == '__main__':
    unittest.main()
