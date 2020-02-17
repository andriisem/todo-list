import json
import unittest

from app import app

class APITestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
    
    def test_status_code(self):
        response = self.app.get('/get')
        self.assertEqual(response.status_code, 200)

    def test_get_type(self):
        response = self.app.get('/get')
        self.assertEqual(response.headers['Content-Type'], 'application/json')

    def test_add_task(self):
        task = 'Task 1'
        response = self.app.post('/add/%s' % task)
        description = response.json['description']
        status = response.json['status']
        self.assertEqual(description, task)
        self.assertEqual(status, False)

    def test_mark_task(self):
        task = 'Task 2'
        response = self.app.post('/add/%s' % task)
        task_id = response.json['id']
        status = response.json['status']
        self.assertEqual(status, False)
        mark_task = self.app.put('/mark/%s/%s' % (task_id, 1))
        status = bool(int(mark_task.json['status']))
        self.assertEqual(status, True)

            
if __name__ == '__main__':
    unittest.main()