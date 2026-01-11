from promptflow import tool

@tool
def run(has_context: bool, llm_output: str):
    """
    This node determines the final message sent to the user.
    If no context was found in search_docs, it returns a hardcoded refusal.
    Otherwise, it returns the LLM's generated response.
    """
    if not has_context:
        return "I can only answer questions related to XXXX."
    
    return llm_output