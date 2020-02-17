import unittest
from unittest.mock import Mock

from app import app, db

class APITestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def test_get(self):
        response = self.app.get('/get')
        self.assertEqual(response.status_code, 200)
    
    def test_get_type(self):
        response = self.app.get('/get')
        self.assertEqual(response.headers['Content-Type'], 'application/json')

    def test_post(self):
        response = self.app.post('/add/task1')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()