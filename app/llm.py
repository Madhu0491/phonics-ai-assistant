import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client =Groq(api_key = api_key)
#print(client.models.list())

def ask_llm(questions:str):
   
    response = client.chat.completions.create(model="openai/gpt-oss-20b",
                                          messages = [{"role":"system","content":"""You are an AI English Phonics Tutor for early readers.Keep anwers short and  simple with short explanations and friendly.Cover the letter sounds,short vowels and cvc words  with examples for  level 1. Generate a question for learners in easy cvc pattern for more interactions.
                            Avoid IPA,Lnguistic terminology,large tables and long explanations Tutor"""},{"role":"user","content":questions}])
    return response.choices[0].message.content
    #print(response)

#print(ask_llm("What is the sound of alphabet e ?"))
