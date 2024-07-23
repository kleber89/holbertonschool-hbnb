import unittest

class TestCity(unittest.TestCase):

    def test_city_creation(self):
        country = Country(name="City's Country")
        city = City(name="Test City", country=country)
        self.assertEqual(city.name, "Test City")
        self.assertEqual(city.country, country)
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)

    def test_country_relation(self):
        country = Country(name="Country With Multiple Cities")
        city1 = City(name="First City", country=country)
        city2 = City(name="Second City", country=country)
        self.assertIn(city1, country.cities)
        self.assertIn(city2, country.cities)

if __name__ == '__main__':
    unittest.main()