import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings())
collection = client.get_or_create_collection("chapters")

def store_version(chapter_id, version_text):
    collection.add(documents=[version_text], ids=[chapter_id])

def search_content(query_text):
    return collection.query(query_texts=[query_text], n_results=1)
