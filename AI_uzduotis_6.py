import os
from dotenv import load_dotenv
from openai import OpenAI
from tiktoken import encoding_for_model

input = "input.txt" 
output = "vertimas.txt"

def read_file(input):
    with open(input, "r", encoding="utf-8") as file:
        content = file.read()
    return content

def count_tokens(text):
    encoding = encoding_for_model("gpt-4")
    tokens = encoding.encode(text)
    return len(tokens)

load_dotenv()
token = os.environ["PASLAPTELE"]

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1" 

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)
tekstas= read_file(input)
if count_tokens(tekstas) > 200:
    print("Tekstas per ilgas, tokio neversiu")
    exit()

# messages = [
#         {
#             "role": "system",
#             "content": "Atsakyk visada lietuviškai."
#         },
#     ]
messages = [
        {
            "role": "system",
            "content": "Išversk tekstą į lietuvių kalbą."
        },
         {
        "role": "user",
        "content": tekstas
    }
    ]

# while True:
#     user_input = input("Įveskite klasimuką (jei norite išeiti įveskite 'exit'): ")
#     if user_input.lower() == "exit":
#         print("Ciao!")
#         break
    
    # messages.append(
    #     {
    #         "role": "user",
    #         "content": user_input
    #     }
    # )
    
response = client.chat.completions.create(
       messages=messages,
       temperature=1,
        top_p=1,
       model=model,
       )
file = open(output, "w", encoding="utf-8")
file.write(response.choices[0].message.content)
file.close()
print("Vertimas jau failiuky")

# print(response.choices[0].message.content)
    