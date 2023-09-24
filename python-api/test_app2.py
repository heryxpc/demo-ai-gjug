import unittest
from unittest.mock import patch
from app import app

class TestLogin(unittest.TestCase):

    @patch('app.csv.DictReader')
    def test_login_success(self, mock_reader):
        mock_reader.return_value = [
            { "username": "heryxpc@gmail.com", "password": "password123"},
            { "username": "orlando@gmail.com", "password": "password123"},  
        ]
        with app.test_client() as client:
            response = client.get('/login?username=heryxpc@gmail.com&password=password123')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, b'True')

    @patch('app.csv.DictReader')
    def test_login_failure(self, mock_reader):
        mock_reader.return_value = [
            { "username": "heryxpc@gmail.com", "password": "password123"},
            { "username": "orlando@gmail.com", "password": "password123"},  
        ]
        with app.test_client() as client:
            response = client.get('/login?username=heryxpc@gmail.com&password=wrongpassword')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, b'False')

if __name__ == '__main__':
    unittest.main()