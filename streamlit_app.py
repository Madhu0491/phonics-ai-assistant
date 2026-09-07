import streamlit as st
from app.llm import ask_llm
st.title("Phonics Assistant")
st.write("Lets learn sounds !!")

#saving the data that is not exist
if "messages" not in st.session_state:
    st.session_state.messages = []
#question = st.text_input("Ask me a phonics question:")
question = st.chat_input("Ask me a phonics question:")   
#condition-chat layer with question
if question:
    st.session_state.messages.append({"role":"user","content":question})#saving users message
    llm_response=ask_llm(messages)#question to llm
    #st.write(llm_response)
    st.session_state.messages.append({"role":"assistant","content":llm_response})

#display the conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])