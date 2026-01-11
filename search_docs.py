from promptflow import tool
from promptflow.connections import CustomConnection
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import os

@tool
def run(question: str, conn: CustomConnection): 

    client = SearchClient(
        endpoint=conn.AZURE_SEARCH_ENDPOINT,
        index_name=conn.AZURE_SEARCH_INDEX,
        credential=AzureKeyCredential(conn.AZURE_SEARCH_KEY)
    )
    # Use the 'question' parameter from your function signature
    results = client.search(search_text=question, top=3)
    docs = [r["chunk"] for r in results if "chunk" in r]

    return {
        "context": "\n\n".join(docs), 
        "has_context": bool(docs)
    }
