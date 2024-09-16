import requests
import unittest
import json
from PIL import Image
import numpy as np

ENDPOINT = 'https://41c6-34-125-136-14.ngrok-free.app/sam2'

class TestImageSegmentationResponse(unittest.TestCase):
    def setUp(self):
        self.url = ENDPOINT
        self.image_path = 'cat+dog.jpg'

    def test_response_format(self):
        with open(self.image_path, 'rb') as image_file:
            files = {'image': image_file}
            response = requests.post(self.url, files=files)

        # Check if the request was successful
        self.assertEqual(response.status_code, 200)

        response_data = response.json()

        response_data = json.loads(response_data)

        # Parse the JSON response
        # response_data = json.loads(response.data)

        # Verify the response is an array
        # self.assertIsInstance(response_data, list)

        # Check each object in the array
        for item in response_data:
            # Verify each item is a dictionary
            self.assertIsInstance(item, dict)
            # Verify the dictionary has a 'segmentation' key
            self.assertIn('segmentation', item)
            # Verify the value associated with 'segmentation' is a list
            self.assertIsInstance(item['segmentation'], list)
            # Check that the segmentation array contains boolean values
            
            segmentation_array = np.array(item['segmentation'])
            self.assertTrue(np.issubdtype(segmentation_array.dtype, np.bool_))
        print('Test 1 passed')
    def test_segmentation_array_size(self):
        with open(self.image_path, 'rb') as image_file:
            files = {'image': image_file}
            response = requests.post(self.url, files=files)

        # Check if the request was successful
        self.assertEqual(response.status_code, 200)

        # Parse the JSON response
        response_data = response.json()

        response_data = json.loads(response_data)

        # Load the image to get its size
        with Image.open(self.image_path) as img:
            width, height = img.size
            expected_size = width * height

        # Verify the size of the segmentation array matches the image size
        for item in response_data:
            segmentation_array = item['segmentation']
            self.assertEqual(len(segmentation_array) * len(segmentation_array[0]), expected_size)
        print('Test 2 passed')

if __name__ == '__main__':
    unittest.main()
