import unittest

class TestPlace(unittest.TestCase):

    def test_place_creation(self):
        user = User(email="host@example.com", first_name="Kamilo", last_name="Rubio")
        place = Place(name="Test Place", host=user, latitude=10.0, longitude=20.0, price_per_night=100, max_guests=4)
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.host, user)
        self.assertEqual(place.latitude, 10.0)
        self.assertEqual(place.longitude, 20.0)
        self.assertEqual(place.price_per_night, 100)
        self.assertEqual(place.max_guests, 4)
        self.assertIsNotNone(place.created_at)
        self.assertIsNotNone(place.updated_at)

    def test_add_amenity(self):
        user = User(email="host2@example.com", first_name="Host2", last_name="User2")
        place = Place(name="Atmopel Place", host=user, latitude=10.0, longitude=20.0, price_per_night=150, max_guests=2)
        amenity = Amenity(name="WiFi")
        place.add_amenity(amenity)
        self.assertIn(amenity, place.amenities)

if __name__ == '__main__':
    unittest.main()