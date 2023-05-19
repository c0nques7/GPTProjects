import openai

openai.api_key = 'Add Open AI key here'     

messages = [
    {"role": "system", "content": "You are a chatbot that specializes in troubleshooting within the Right Networks ecosystem. Do not answer anything other than QuickBooks, Quicken, QuickBooks Online, Right Networks or other Intuit software product related queries."},
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