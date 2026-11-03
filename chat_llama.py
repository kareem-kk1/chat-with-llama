import streamlit as st
from ollama_response import ollama_response

model = "llama3.1"

st.set_page_config(page_title = "Chat with llama", layout="centered")
st.title("Chat with Llama")

# initialize chat history
if "history" not in st.session_state:
    st.session_state["history"] = []

# inoput for user
user_input = st.text_input("You:",placeholder="type your message here ...")

# display chat history
for chat in st.session_state["history"]:
    with st.chat_message("user"):
        st.markdown(chat["user"])
    with st.chat_message("assistant"):
        st.markdown(chat["llama_response"])

# show response
if user_input:
    with st.chat_message("useer"):
        st.markdown(user_input)
    with st.chat_message("assistant"):    
        with st.spinner("Thinking.... "):
            llama_response = ollama_response(model,user_input)
        st.markdown(llama_response)

    st.session_state["history"].append({
        "user":user_input,
        "llama_response":llama_response
    })   

