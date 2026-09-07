import streamlit as st

st.title("Phonics Assistant")

if "messages" not  in st.session_state:
    st.session_state.messages = []

question = st.chat_input("Ask me a phonics questions")

if question:
    st.session_state.messages.append({"role":"user","content":question})
with st.chat_message("user"):
    st.write("")

for message in st.session_state.messages:
    with st.chat_message("role"):
        st.write(message["content"])


