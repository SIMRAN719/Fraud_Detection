import openai
from dotenv import load_dotenv
import os
#API Key 
API_KEY = os.getenv('API_key')
openai.api_key=API_KEY
messages=[{"role": "system", "content": "You are a helpful and kind assistant."}]
while True:
    message=input("user :")
    if message:
        messages.append({'role':'user','content':message},)
        response = openai.chat.completions.create(model="gpt-3.5-turbo",messages=messages)
        reply=response.choices[0].message.content
        print('chatbot : {}'.format(reply))
        messages.append({'role':'assistant','content':reply})