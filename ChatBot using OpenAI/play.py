import openai
#Use your personal API Key
API_key='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'
openai.api_key=API_key
messages=[{"role": "system", "content": "You are a helpful and kind assistant."}]
while True:
    message=input("user :")
    if message:
        messages.append({'role':'user','content':message},)
        response = openai.chat.completions.create(model="gpt-3.5-turbo",messages=messages)
        reply=response.choices[0].message.content
        print('chatbot : {}'.format(reply))
        messages.append({'role':'assistant','content':reply})