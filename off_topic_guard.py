from promptflow import tool

@tool
def run(has_context: bool): # Changing 'Input1' to 'has_context' here updates the UI
    return has_context
