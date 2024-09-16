import requests
import base64
import json

# Replace with the actual URL of your Flask app
url = "http://127.0.0.1:5000/sketch-to-image"

# URL of the image to download
image_url = "https://storage.googleapis.com/mle-courses-prod/users/61b869ca9c3c5e00292bb42d/private-files/01cc2190-4329-11ef-bf69-71eafa46c86b-Screen_Shot_2024_07_16_at_11.08.02.png"

# Download the image
response = requests.get(image_url)
response.raise_for_status()  # Ensure we got a valid response

# Encode the image in base64
base64_image = base64.b64encode(response.content).decode('utf-8')

# Define the payload
payload = {
    "base64": base64_image,
    "prompt": "Create an anime-style illustration of a car. The background should have a gradient effect from green to blue, with a glowing light source in the top corner, adding a magical ambiance. The car should have bright, vibrant colors include small, sparkling light particles around the scene to enhance the enchanting feel. The overall style should be soft and colorful, with a whimsical, dreamy atmosphere.",
    "negative_prompt": "",
    "control_strength": 1,
    "seed": 0,
    "output_format": "webp"
}

# Set the headers
headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check the response status code
assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

# Parse the JSON response
response_json = response.json()

# Check that the 'image' key is present and contains a base64 string
assert 'image' in response_json, "Response JSON does not contain 'image' key"
assert isinstance(response_json['image'], str), "'image' key does not contain a string"
try:
    base64.b64decode(response_json['image'])
except Exception as e:
    assert False, "'image' key does not contain a valid base64-encoded string"

# Check that the 'seed' key is present
assert 'seed' in response_json, "Response JSON does not contain 'seed' key"

# Print a success message
print("Test passed successfully")
