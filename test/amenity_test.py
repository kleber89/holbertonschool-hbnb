import unittest

class TestAmenity(unittest.TestCase):

    def test_amenity_creation(self):
        amenity = Amenity(name="Swimming Pool")
        self.assertEqual(amenity.name, "Swimming Pool")
        self.assertIsNotNone(amenity.created_at)
        self.assertIsNotNone(amenity.updated_at)

if __name__ == '__main__':
    unittest.main()