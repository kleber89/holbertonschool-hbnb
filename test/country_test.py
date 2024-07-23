import unittest

class TestCountry(unittest.TestCase):

    def test_country_creation(self):
        country = Country(name="Test Country")
        self.assertEqual(country.name, "Test Country")
        self.assertIsNotNone(country.created_at)
        self.assertIsNotNone(country.updated_at)

    def test_add_city(self):
        country = Country(name="Country With City")
        city = City(name="City in Country", country=country)
        self.assertIn(city, country.cities)

if __name__ == '__main__':
    unittest.main()