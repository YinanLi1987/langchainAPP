from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from load_data import docs
from settings import Config


text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000)
chunked_docs = text_splitter.split_documents(docs)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small",openai_api_key=Config.OPENAI_API_KEY)
vectorstore = Chroma.from_documents(
    chunked_docs,
    embeddings,
)
