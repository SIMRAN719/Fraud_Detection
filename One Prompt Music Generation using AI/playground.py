from requests import post
from pydub import AudioSegment
from io import BytesIO

#Hugging face
API="https://api-inference.huggingface.co/models/facebook/musicgen-small"
#My API Key
API_key="Bearer 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"
song=input("Enter which type of music you want to listen :")
a=post(API,headers={"Authorization":API_key},json={'inputs':song})
b=AudioSegment.from_file(BytesIO(a.content))
b.export("new_music.mp3",format="mp3")