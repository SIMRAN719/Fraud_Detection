import requests
import io
from PIL import Image
import random
from dotenv import load_dotenv
import os

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
apikey = os.getenv('API_Key')

def query(payload):
    response = requests.post(API_URL, headers={'Authorization': "Bearer {}".format(apikey)}, json=payload)
    return response.content

def generate_image(prompt):
    seed = random.randint(1, 1000)
    random.seed(seed)
    payload = {"inputs": prompt, 'parameters': {'temperature': random.uniform(0.5, 1.5)}}
    image_bytes = query(payload)
    
    print("Content received from API:", image_bytes)  # Print content received from API
    
    try:
        # Attempt to open the image using PIL
        image = Image.open(io.BytesIO(image_bytes))
        return image
    except Exception as e:
        print("Error:", e)
        return None

pmt = input("Enter your prompt: ")
image = generate_image(pmt)

if image is not None:
    image.show()
    image.save("pic.png")
else:
    print("Failed to generate the image.")
