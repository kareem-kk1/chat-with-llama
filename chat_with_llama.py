
import streamlit as st
from llama_call import llama_response

model = "llama3.1"

st.set_page_config(
    page_title="Chat with Llama",
    layout="centered"
)

st.title("Chat with Llama 🦙")
st.caption("Conversational AI with memory")

# Initialize conversation memory
if "history" not in st.session_state:
    st.session_state.history = []

# Clear chat history
if st.button("Clear Chat"):
    st.session_state.history = []
    st.rerun()

# Display previous conversation
for chat in st.session_state.history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# User input
user_input = st.chat_input("Ask me anything...")

if user_input:

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Add user message to memory
    st.session_state.history.append({
        "role": "user",
        "content": user_input
    })

    # Generate response using conversation history
    with st.chat_message("assistant"):
        with st.spinner("Llama is thinking..."):

            response = llama_response(
                model,
                st.session_state.history
            )

            st.markdown(response)

    # Save assistant response to memory
    st.session_state.history.append({
        "role": "assistant",
        "content": response
    })
