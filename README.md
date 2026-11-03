# 🦙 Chat with Llama – Conversational AI Chatbot

A conversational AI chatbot built using **Python, Streamlit, and Ollama (Llama 3.1)**. The application maintains conversation history and uses previous messages as context to generate relevant, context-aware responses.

Unlike a basic question-answering application, this chatbot can remember earlier messages within the current session and respond based on previous conversations.

## 🚀 Features

- **Conversational AI:** Interact with Meta's Llama 3.1 model locally using Ollama.
- **Conversation Memory:** Maintains previous user and assistant messages.
- **Context-Aware Responses:** Uses conversation history to answer follow-up questions.
- **ChatGPT-Style Interface:** Interactive chat interface built with Streamlit.
- **Session Management:** Preserves conversation history during Streamlit reruns.
- **Clear Chat:** Reset the conversation whenever needed.
- **Local Execution:** Run the LLM locally through Ollama without relying on cloud-based AI APIs.

## 🛠️ Tech Stack

| Technology              | Purpose                       |
| ----------------------- | ----------------------------- |
| Python                  | Backend development           |
| Streamlit               | Interactive chatbot interface |
| Ollama                  | Local LLM execution           |
| Llama 3.1               | Language generation           |
| Streamlit Session State | Conversation memory           |

## 📂 Project Structure

```text
chat-with-llama/
│
├── chat_with_llama.py      # Main Streamlit application
├── llama_call.py           # Ollama model integration
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/kareem-kk1/chat-with-llama.git
```

Navigate to the project directory:

```bash
cd chat-with-llama
```

### 2. Create a Python virtual environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install streamlit ollama
```

Alternatively, if using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download and install Ollama:

https://ollama.com/download

### 5. Download the Llama 3.1 model

Open your terminal and execute:

```bash
ollama pull llama3.1
```

Verify the installed model:

```bash
ollama list
```

### 6. Run the application

Start the Streamlit application:

```bash
streamlit run chat_with_llama.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## 💬 Example Conversation

The chatbot maintains context throughout the conversation.

**User:**
What is Artificial Intelligence?

**Llama:**
Artificial Intelligence (AI) is a branch of computer science that enables machines to perform tasks that typically require human intelligence, such as learning, reasoning, problem-solving, and understanding language.

**User:**
Can you give me two real-world applications?

**Llama:**
Certainly! Here are two real-world applications of Artificial Intelligence:

1. **Healthcare:** AI helps doctors analyze medical images, detect diseases, and support clinical decision-making.
2. **Virtual Assistants:** AI powers assistants that understand voice commands, answer questions, and help users perform everyday tasks.

## 🔮 Future Enhancements

🧠 How Conversation Memory Works

The application uses Streamlit Session State to maintain conversation history throughout an active chat session.

Every user message and assistant response is stored as a dictionary containing a role and content.

1. Storing Conversation History

User messages are stored with the user role:

{
    "role": "user",
    "content": "What is Artificial Intelligence?"
}

Assistant responses are stored with the assistant role:

{
    "role": "assistant",
    "content": "Artificial Intelligence enables machines to perform tasks that typically require human intelligence."
}

2. Maintaining Context

The application maintains all previous messages in Streamlit's session state:

st.session_state.history.append({
    "role": "user",
    "content": user_input
})

After generating a response, the assistant's message is also added to the conversation history.

st.session_state.history.append({
    "role": "assistant",
    "content": response
})

3. Generating Context-Aware Responses

The complete conversation history is passed to Ollama through its chat interface:

response = ollama.chat(
    model=model,
    messages=st.session_state.history
)

Llama 3.1 processes the previous messages along with the latest user query to generate relevant, context-aware responses.

For example, if a user asks about Artificial Intelligence, then asks about its applications, and later refers to one of those applications, Llama can use the earlier conversation to understand the context.

4. Memory Management

The application provides session-based conversation memory with the following capabilities:

Stores previous user and assistant messages.

Retains conversation context during Streamlit reruns.

Supports follow-up questions based on earlier messages.

Displays the complete conversation in the chat interface.

Allows users to clear the conversation using the Clear Chat button.

Note: This implementation uses temporary, session-based memory rather than permanent storage. Conversation history is not saved to a database and may be lost when the session ends or the application restarts.

- Persistent conversation storage using SQLite.
- Long-term memory across multiple chat sessions.
- Semantic search using ChromaDB.
- Conversation summarization for managing large chat histories.
- Multiple chat sessions and conversation management.
- Support for additional Ollama models.
- Custom system prompts and chatbot personalities.

## 👨‍💻 Author

**Mohammad Kareem Khan**

Data Scientist | Generative AI Engineer

- GitHub: [kareem-kk1](https://github.com/kareem-kk1)
- LinkedIn: [Mohammad Kareem Khan](https://linkedin.com/in/kareem-khan-mohammad)

## 📄 License

This project is open-source and available for learning and educational purposes. You can modify and extend it for your own applications.
