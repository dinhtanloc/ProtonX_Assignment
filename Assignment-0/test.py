import unittest
import requests

class TestCatAPI(unittest.TestCase):
    BASE_URL = 'http://127.0.0.1:5002'  # Update this if your server is hosted elsewhere

    def test_get_all_cats(self):
        response = requests.get(f'{self.BASE_URL}/cats')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_get_cat_by_id(self):
        response = requests.get(f'{self.BASE_URL}/cats/cat1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('name', response.json())
        self.assertEqual(response.json()['name'], 'Fluffy')

    def test_get_cat_by_invalid_id(self):
        response = requests.get(f'{self.BASE_URL}/cats/invalid_id')
        self.assertEqual(response.status_code, 404)

    def test_create_cat(self):
        new_cat = {
            'name': 'Shadow',
            'age': 1,
            'image_link': 'https://example.com/shadow.png'
        }
        response = requests.post(f'{self.BASE_URL}/cats', json=new_cat)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json())
        self.assertEqual(response.json()['name'], 'Shadow')

    def test_create_cat_invalid_request(self):
        new_cat = {
            'age': 1
        }
        response = requests.post(f'{self.BASE_URL}/cats', json=new_cat)
        self.assertEqual(response.status_code, 400)

    def test_update_cat(self):
        updated_cat = {
            'name': 'Fluffy Jr.',
            'age': 3,
            'image_link': 'https://example.com/fluffy_jr.png'
        }
        response = requests.put(f'{self.BASE_URL}/cats/cat1', json=updated_cat)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'Fluffy Jr.')

    def test_patch_cat(self):
        patch_data = {
            'age': 5
        }
        response = requests.patch(f'{self.BASE_URL}/cats/cat2', json=patch_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['age'], 5)

    def test_delete_cat(self):
        response = requests.delete(f'{self.BASE_URL}/cats/cat3')
        self.assertEqual(response.status_code, 204)
        # Verify cat is deleted
        follow_up_response = requests.get(f'{self.BASE_URL}/cats/cat3')
        self.assertEqual(follow_up_response.status_code, 404)

    def test_delete_cat_invalid_id(self):
        response = requests.delete(f'{self.BASE_URL}/cats/invalid_id')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
    
