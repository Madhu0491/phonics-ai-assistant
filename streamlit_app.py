import streamlit as st
from app.llm import ask_llm
st.title("Phonics Assistant")
st.write("Lets learn sounds !!")
st.sidebar.title("Phonics Chapters")
lesson = st.sidebar.selectbox("Choose a lesson:",["Letter Sounds","Short Vowels","CVC words"])
mode = st.sidebar.selectbox("Choose the mode:",["Chat","Practice"])
#creatng separate chat history for each lesson 
if "lesson_messages" not in st.session_state:
    st.session_state.lesson_messages = {
        "Letter Sounds":[],"Short Vowels" :[],"CVC words":[]
        }

question = st.chat_input("Ask me a phonics question:")   

if question:
    #Add users message to particular lesson
    st.session_state.lesson_messages[lesson].append({"role":"user","content":question})
    #sending only selected lesson chat history to llm
    llm_response=ask_llm( st.session_state.lesson_messages[lesson],lesson)
    #adding the llm_response to the selected particular lesson
    st.session_state.lesson_messages[lesson].append({"role":"assistant","content":llm_response})

#display the conversation
for message in st.session_state.lesson_messages[lesson]:
    with st.chat_message(message["role"]):
        st.write(message["content"])