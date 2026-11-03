import ollama

def llama_response(model: str, messages: list) -> str:
    """
    Generates a context-aware response using Ollama.

    Args:
        model: Ollama model name.
        messages: Previous conversation messages.

    Returns:
        Generated assistant response.
    """
    try:
        response = ollama.chat(
            model=model,
            messages=messages
        )

        return response["message"]["content"]

    except Exception as e:
        return f"[Error] {str(e)}"
