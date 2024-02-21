import requests
import io
from PIL import Image
import random
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
API_Key="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"

def query(payload):
	response = requests.post(API_URL, headers={'Authorization':"Bearer {}".format(API_Key)}, json=payload)
	return response.content
def generate_image(prompt):
    seed=random.randint(1,1000)
    random.seed(seed)
    payload={"inputs": prompt,'parameters':{'temperature':random.uniform(0.5,1.5)}}
    '''
    payload={"inputs": prompt,'parameters':{'temperature':random.uniform(0.5,1.5),
            'top_p': random.uniform(0.8,1.0),
            'num_beams': random.randint(1,5),
            'diversity_penalty': random.uniform(0.5,1.5)}}'''
    image_bytes = query(payload)
    image = Image.open(io.BytesIO(image_bytes))
    return image
pmt=input("Enter you prompt :")
image=generate_image(pmt)
image.show()
image.save("pic.png")