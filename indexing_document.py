from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from settings import Config
import json
import os
from langchain_core.documents import Document

current_directory = os.path.dirname(__file__)
folder_path = os.path.join(current_directory, "docs_json")

# Read content from each JSON file and store in a list of MyDocument objects
docs = []
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            # Load JSON content from the file
            json_data = json.load(file)
             # Extract page content and metadata from JSON data
            page_content = json_data.get("page_content", "")
            metadata = json_data.get("metadata", {})
            # Create a Document object and append it to the list
            doc = Document(page_content=page_content, metadata=metadata)
            docs.append(doc)


text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000)
chunked_docs = text_splitter.split_documents(docs)


   

embeddings = OpenAIEmbeddings(model="text-embedding-3-small",openai_api_key=Config.OPENAI_API_KEY)
vectorstore = Chroma.from_documents(
    chunked_docs,
    embeddings,
)
search_results = vectorstore.similarity_search("which CR is from Mediatek?")
print(search_results[0].metadata)
print(search_results[1].metadata)
print(search_results[2].metadata)

