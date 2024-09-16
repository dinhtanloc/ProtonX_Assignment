from flask import Flask, request, jsonify
import requests
from PIL import Image
import io
import base64
import time
import json
import os
import tempfile
from flask_cors import CORS
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

app = Flask(__name__)
CORS(app)

# Get the key from https://platform.stability.ai/account/keys
STABILITY_KEY = os.getenv('STABILITY_KEY')
# print(STABILITY_KEY)
#@title Define functions

def send_generation_request(
    host,
    params,
):
    headers = {
        "Accept": "image/*",
        "Authorization": f"Bearer {STABILITY_KEY}"
    }

    # Encode parameters
    files = {}
    image = params.pop("image", None) # /content/IMG_6634.jpg
    mask = params.pop("mask", None)
    if image is not None and image != '':
        files["image"] = open(image, 'rb')
    if mask is not None and mask != '':
        files["mask"] = open(mask, 'rb')
    if len(files)==0:
        files["none"] = ''

    # Send request
    print(f"Sending REST request to {host}...")
    response = requests.post(
        host,
        headers=headers,
        files=files,
        data=params
    )
    if not response.ok:
        raise Exception(f"HTTP {response.status_code}: {response.text}")

    return response

def send_async_generation_request(
    host,
    params,
):
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {STABILITY_KEY}"
    }

    # Encode parameters
    files = {}
    if "image" in params:
        image = params.pop("image")
        files = {"image": open(image, 'rb')}

    # Send request
    print(f"Sending REST request to {host}...")
    response = requests.post(
        host,
        headers=headers,
        files=files,
        data=params
    )
    if not response.ok:
        raise Exception(f"HTTP {response.status_code}: {response.text}")

    # Process async response
    response_dict = json.loads(response.text)
    generation_id = response_dict.get("id", None)
    assert generation_id is not None, "Expected id in response"

    # Loop until result or timeout
    timeout = int(os.getenv("WORKER_TIMEOUT", 500))
    start = time.time()
    status_code = 202
    while status_code == 202:
        response = requests.get(
            f"{host}/result/{generation_id}",
            headers={
                **headers,
                "Accept": "image/*"
            },
        )

        if not response.ok:
            raise Exception(f"HTTP {response.status_code}: {response.text}")
        status_code = response.status_code
        time.sleep(10)
        if time.time() - start > timeout:
            raise Exception(f"Timeout after {timeout} seconds")

    return response

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get("prompt", "op art cat illusion red blue chromostereopsis maximum saturation")
    negative_prompt = data.get("negative_prompt", "")
    aspect_ratio = data.get("aspect_ratio", "21:9")
    seed = data.get("seed", 0)
    output_format = data.get("output_format", "png")

    host = f"https://api.stability.ai/v2beta/stable-image/generate/core"

    params = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "aspect_ratio": aspect_ratio,
        "seed": seed,
        "output_format": output_format
    }

    try:
        response = send_generation_request(host, params)
        output_image = response.content
        finish_reason = response.headers.get("finish-reason")
        seed = response.headers.get("seed")

        if finish_reason == 'CONTENT_FILTERED':
            return jsonify({"error": "Generation failed NSFW classifier"}), 400

        # Convert image to base64
        generated = io.BytesIO(output_image)
        generated.seek(0)
        img = Image.open(generated)
        buffered = io.BytesIO()
        img.save(buffered, format=output_format.upper())
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

        return jsonify({"b64_json": img_str, "seed": seed})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


@app.route('/sketch-to-image', methods=['POST'])
def sketch_to_image():
    try:
        data = request.get_json()
        base64_image = data.get('base64')

        if not base64_image:
            return jsonify({'error': 'No image data found'}), 400

        # TODO 1: Nhận ảnh từ client và lưu ảnh thành file.png
        image_data = base64.b64decode(base64_image)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_image:
            temp_image.write(image_data)
            temp_image.flush()
            image_path = temp_image.name

        # image = None
        # image_path = None

        prompt = data.get('prompt', 'Create an anime-style illustration of a car. The background should have a gradient effect from green to blue, with a glowing light source in the top corner, adding a magical ambiance. The car should have bright, vibrant colors include small, sparkling light particles around the scene to enhance the enchanting feel. The overall style should be soft and colorful, with a whimsical, dreamy atmosphere.')
        negative_prompt = data.get('negative_prompt', '')
        control_strength = data.get('control_strength', 1)
        seed = data.get('seed', 0)
        output_format = data.get('output_format', 'webp')

        host = "https://api.stability.ai/v2beta/stable-image/control/sketch"
        # host = "https://api.stability.ai/v2beta/stable-image/generate/ultra"

        params = {
            "control_strength": control_strength,
            "image": image_path,
            "seed": seed,
            "output_format": output_format,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
        }

        response = send_generation_request(host, params)

        # Decode response
        output_image = response.content
        finish_reason = response.headers.get("finish-reason")
        seed = response.headers.get("seed")

        # Check for NSFW classification
        if finish_reason == 'CONTENT_FILTERED':
            return jsonify({'error': 'Generation failed NSFW classifier'}), 400

        # Save and display result
        # TODO 2: Lấy ảnh từ respone của Stability, chuyển thành Base64 và gửi về client
        img = Image.open(io.BytesIO(output_image))
        buffered = io.BytesIO()
        img.save(buffered, format=output_format.upper())
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

        
        return jsonify({"image": img_str, "seed": seed})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
