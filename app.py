from flask import Flask, request, jsonify
from diffusers import StableDiffusionPipeline
import torch
import base64
from io import BytesIO
from PIL import Image
import time
import os

# Initialize Flask app
app = Flask(__name__)

# Load the Stable Diffusion pipeline from pre-downloaded files
model_path = "./model/"

print("Loading model from", model_path)
pipe = StableDiffusionPipeline.from_pretrained(
    model_path, torch_dtype=torch.float16
).to("cuda")


import torch
if not torch.cuda.is_available():
    raise Exception("CUDA is not available. Please install CUDA and cuDNN.")

print("Torch device name: " + torch.cuda.get_device_name(0))  # Should print your GPU name


@app.route("/generate", methods=["POST"])
def generate_image():
    data = request.json
    if not data or "prompt" not in data:
        return jsonify({"error": "Invalid input, 'prompt' is required"}), 400

    prompt = data["prompt"]
    try:
        start_time = time.time()
        # Generate the image
        with torch.no_grad():
            image = pipe(prompt, num_inference_steps=20).images[0]
        end_time = time.time()
        generation_time = end_time - start_time

        # Convert image to base64
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return jsonify({"prompt": prompt, "image": img_str, "generation_time": generation_time})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run the app
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
