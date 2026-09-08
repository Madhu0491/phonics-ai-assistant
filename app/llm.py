import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client =Groq(api_key = api_key)
#print(client.models.list())

def ask_llm(messages,lesson):
    system_mesage = {"role":"system",
                     "content":f"""You are a friendly, accurate phonics tutor for early learners.
                     Lesson:{lesson}.
                     Rules:
                     1)Use simple ,age-appropriate language.
                     2)Stay focused on selected lesson
                     3)Give accurate phonics exaplanations and examples.
                     4)Clearly distinguish short and long vowels
                     5)Avoid IPA unless required
                     6)Never give contradictory or invented phonics rules.
                     7)Keep answers concise and include a short practice activity when useful.Teach the child according to the selected lesson.
                     Use simple explanations and examples suitable for beginners."""
        }
   #client.chat.completions.create is an actual API call to Groq's LLM.
    response = client.chat.completions.create(model="openai/gpt-oss-20b",
                                          messages = [system_mesage]+messages)
    return response.choices[0].message.content
    #print(response)

#print(ask_llm("What is the sound of alphabet e ?"))
