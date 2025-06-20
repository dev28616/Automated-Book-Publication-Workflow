from storage.chromadb_utils import search_content

def intelligent_search(prompt):
    result = search_content(prompt)
    return result["documents"][0][0] if result["documents"] else "No result found."
