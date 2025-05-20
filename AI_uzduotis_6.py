import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
token = os.environ["PASLAPTELE"]

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1" 

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)
messages = [
        {
            "role": "system",
            "content": "Atsakyk visada lietuviškai."
        },
    ]

while True:
    user_input = input("Įveskite klasimuką (jei norite išeiti įveskite 'exit'): ")
    if user_input.lower() == "exit":
        print("Ciao!")
        break
    
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    
    response = client.chat.completions.create(
       messages=messages,
       temperature=1,
        top_p=1,
       model=model,
       )
    

    print(response.choices[0].message.content)
    