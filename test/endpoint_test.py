import unittest
import json
from app import app, data_manager
from models import User

class UserApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        data_manager.storage['User'] = {}  # Reset storage before each test

    def test_create_user(self):
        response = self.app.post('/users/', 
                                 data=json.dumps({'email': 'test@example.com', 'first_name': 'John', 'last_name': 'Doe'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_user(self):
        user = User(id=1, email='test@example.com', first_name='John', last_name='Doe')
        data_manager.save(user)
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('test@example.com', str(response.data))

    def test_update_user(self):
        user = User(id=1, email='test@example.com', first_name='John', last_name='Doe')
        data_manager.save(user)
        response = self.app.put('/users/1',
                                data=json.dumps({'email': 'test2@example.com', 'first_name': 'John', 'last_name': 'Smith'}),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('test2@example.com', str(response.data))

    def test_delete_user(self):
        user = User(id=1, email='test@example.com', first_name='John', last_name='Doe')
        data_manager.save(user)
        response = self.app.delete('/users/1')
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(data_manager.get(1, 'User'))

if __name__ == '__main__':
    unittest.main()