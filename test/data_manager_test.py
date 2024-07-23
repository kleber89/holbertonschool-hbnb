import unittest

class TestDataManager(unittest.TestCase):

    def setUp(self):
        self.data_manager = DataManager()

    def test_save_and_get_user(self):
        user = User(id=1, email="test@example.com", first_name="John", last_name="Doe")
        self.data_manager.save(user)
        retrieved_user = self.data_manager.get(1, 'User')
        self.assertEqual(user, retrieved_user)

    def test_update_user(self):
        user = User(id=2, email="update@example.com", first_name="Jane", last_name="Smith")
        self.data_manager.save(user)
        user.first_name = "Janet"
        self.data_manager.update(user)
        updated_user = self.data_manager.get(2, 'User')
        self.assertEqual(updated_user.first_name, "Janet")

    def test_delete_user(self):
        user = User(id=3, email="delete@example.com", first_name="Alice", last_name="Johnson")
        self.data_manager.save(user)
        self.data_manager.delete(3, 'User')
        deleted_user = self.data_manager.get(3, 'User')
        self.assertIsNone(deleted_user)

    def test_save_and_get_place(self):
        user = User(id=4, email="host@example.com", first_name="Host", last_name="User")
        self.data_manager.save(user)
        place = Place(id=1, name="Test Place", host=user)
        self.data_manager.save(place)
        retrieved_place = self.data_manager.get(1, 'Place')
        self.assertEqual(place, retrieved_place)

    def test_save_and_get_country_city(self):
        country = Country(id=1, name="Test Country")
        city = City(id=1, name="Test City", country=country)
        self.data_manager.save(country)
        self.data_manager.save(city)
        retrieved_country = self.data_manager.get(1, 'Country')
        retrieved_city = self.data_manager.get(1, 'City')
        self.assertEqual(country, retrieved_country)
        self.assertEqual(city, retrieved_city)
        self.assertEqual(city.country, retrieved_country)

if __name__ == '__main__':
    unittest.main()