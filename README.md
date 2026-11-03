
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
├── ollama_response.py      # Ollama model integration
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
My name is Kareem.

**Llama:**
Nice to meet you, Kareem!

**User:**
I am learning Python.

**Llama:**
That's great! Python is a versatile programming language.

**User:**
What is my name?

**Llama:**
Your name is Kareem.

**User:**
What am I learning?

**Llama:**
You are learning Python.

## 🧠 How Conversation Memory Works

The application uses Streamlit's session state to store conversation history.

Each message is stored with a role and content:

```python
{
    "role": "user",
    "content": "My name is Kareem."
}
```

```python
{
    "role": "assistant",
    "content": "Nice to meet you, Kareem!"
}
```

The stored conversation is passed to Ollama using its chat interface:

```python
response = ollama.chat(
    model=model,
    messages=messages
)
```

This allows Llama to use previous messages as context when generating new responses.

**Note:** This implementation provides session-based memory. Conversation history is not permanently stored and will be lost when the Streamlit session is reset or the application restarts.

## 🔮 Future Enhancements

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
