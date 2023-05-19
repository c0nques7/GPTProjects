import openai

openai.api_key = 'Add Open AI KEY HERE'     

messages = [
    {"role": "system", "content": "You are a chatbot that specializes in troubleshooting within the Microsoft ecosystem. Do not answer anything other than Microsoft Windows, Office or other Microsoft software product related queries."},
]
     

while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})