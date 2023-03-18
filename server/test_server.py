import unittest
import json
from app import app

class TestTodos(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_todos(self):
        response = self.app.get('/todos')
        self.assertEqual(response.status_code, 200)
        todos = json.loads(response.data)
        self.assertTrue(isinstance(todos, list))

    def test_add_todo(self):
        todo = {'title': 'Test Todo', 'body': 'Test Body'}
        response = self.app.post('/todos', data=json.dumps(todo), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        added_todo = json.loads(response.data)
        self.assertEqual(added_todo['title'], todo['title'])
        self.assertEqual(added_todo['body'], todo['body'])

if __name__ == '__main__':
    unittest.main()