import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from together import Together


# Khi build docker, trong docker-compose.yaml sẽ cần định nghĩa API_TOKEN
api_token = os.getenv("API_TOKEN")

# Initialize Together client
client = Together(api_key=api_token)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json  # Get the JSON payload
    image_url = data.get('image_url', None)  # Extract the image URL
    prompt = data.get('prompt', '')  # Extract the prompt

    if image_url:
        # Call Together API for image-based text extraction with prompt
        response_content = extract_text_with_prompt_from_image(image_url, prompt)
    else:
        return jsonify({"error": "No image URL provided"}), 400

    return jsonify({
        "content": response_content,
        "role": "assistant"
    })

def extract_text_with_prompt_from_image(image_url, prompt):
    # Send request to Together API using the provided image URL and prompt
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt if prompt else "Extract the text from the image"
                    },
                    {
                        "type": "image_url",  # Provide the image URL from JSON
                        "image_url": {
                            "url": image_url
                        }
                    }
                ]
            }
        ],
        max_tokens=512,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>", "<|eom_id|>"],
    )

    return response.choices[0].message.content if response.choices else "Unable to process the image with the provided prompt."

if __name__ == "__main__":
    # Quan trọng, build docker phải đặt host bằng "0.0.0.0"
    app.run(host="0.0.0.0", port=5002)