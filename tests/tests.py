import unittest
from flask import current_app
from base64 import b64encode
import requests, json


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.VERSION = 'v1.0'
        self.BASE_URL = 'http://127.0.0.1:5000/api/' + self.VERSION
        self.headers={'content-type': 'application/json'}

    def tearDown(self):
        pass

    def get_api_headers(self, username, password):
        return {
            'Authorization': 'Basic ' + b64encode(
                (username + ':' + password).encode('utf-8')).decode('utf-8'),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    # Did our app instantiate correctly?
    def test_app_exists(self):
        self.assertFalse(current_app is None)

    # Bad URLs should throw a 404
    def test_404(self):
        r = requests.get(self.BASE_URL + '/does/not/exist')
        self.assertTrue(r.status_code == 404)

    def test_goal(self):
        url = self.BASE_URL + '/goal'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

        payload = {
            'date': '20141012',
            'weight': 179
        }
        r = requests.put(url, json.dumps(payload), headers=self.headers)
        # Assumes you already started with test data
        self.assertTrue(r.status_code == 400)

        payload = {'date': '20141012', 'weight': 201}
        r = requests.patch(url, json.dumps(payload), headers=self.headers)
        self.assertTrue(r.status_code == 204)

    def test_weight(self):
        url = self.BASE_URL + '/weight'

        payload = {
            'date': '20141013',
            'weight': 179
        }
        r = requests.put(url, json.dumps(payload), headers=self.headers)
        # Assumes you already started with test data
        self.assertTrue(r.status_code == 400)

        payload = {'date': '20141012', 'weight': 201}
        r = requests.patch(url, json.dumps(payload), headers=self.headers)
        self.assertTrue(r.status_code == 204)

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

    def test_calories(self):
        url = self.BASE_URL + '/calories'

        payload = {
            'date': '20141013',
            'calories': 100
        }
        r = requests.put(url, json.dumps(payload), headers=self.headers)
        # Assumes you already started with test data
        self.assertTrue(r.status_code == 400)

        payload = {'date': '20141014', 'calories': -200}
        r = requests.patch(url, json.dumps(payload), headers=self.headers)
        self.assertTrue(r.status_code == 204)

        payload = {'date': '20141013', 'calories': 300}
        r = requests.patch(url, json.dumps(payload), headers=self.headers)
        self.assertTrue(r.status_code == 204)

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

if __name__ == '__main__':
    unittest.main()