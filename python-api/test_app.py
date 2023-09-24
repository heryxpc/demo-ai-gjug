import unittest
from app import app

class TestLogin(unittest.TestCase):

    def test_login_success(self):
        with app.test_client() as client:
            response = client.get('/login?username=heryxpc@gmail.com&password=password123')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, b'True')

    def test_login_failure(self):
        with app.test_client() as client:
            response = client.get('/login?username=heryxpc@gmail.com&password=wrongpassword')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, b'False')

if __name__ == '__main__':
    unittest.main()