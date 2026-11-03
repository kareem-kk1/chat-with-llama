import ollama

def ollama_response(model: str, prompt: str) -> str:
    """
    Generates a response from the given Ollama model.

    Args:
        model (str): The model name (e.g., "llama3.1").
        prompt (str): The input prompt for the model.

    Returns:
        str: The generated response from the model, or an error message.
    """
    try:
        response = ollama.generate(
            model=model,
            prompt=prompt
        )
        return response.get("response", "[No response key in result]")
    except Exception as e:
        return f"[Error] {str(e)}"
