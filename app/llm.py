import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client =Groq(api_key = api_key)
#print(client.models.list())

def ask_llm(messages,lesson):
    system_mesage = {"role":"system",
                     "content":f"""You are a friendly phonics tutor.
                     The current lesson is: {lesson}.Teach the child according to the selected lesson.
                     Use simple explanations and examples suitable for beginners."""
        }
   #client.chat.completions.create is an actual API call to Groq's LLM.
    response = client.chat.completions.create(model="openai/gpt-oss-20b",
                                          messages = [system_mesage]+messages)
    return response.choices[0].message.content
    #print(response)

#print(ask_llm("What is the sound of alphabet e ?"))
