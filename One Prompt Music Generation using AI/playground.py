from requests import post
from pydub import AudioSegment
from io import BytesIO
from dotenv import load_dotenv
import os
#Hugging face
API="https://api-inference.huggingface.co/models/facebook/musicgen-small"
#My API Key
API_Key=os.getenv('API_Key')
song=input("Enter which type of music you want to listen :")
a=post(API,headers={"Authorization":API_Key},json={'inputs':song})
b=AudioSegment.from_file(BytesIO(a.content))
b.export("new_music.mp3",format="mp3")