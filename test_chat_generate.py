from langchain_openai import ChatOpenAI
from settings import Config
from langchain_core.prompts import ChatPromptTemplate
from typing import List
from langchain_core.documents import Document
from indexing_document import vectorstore
from query_schema import Search


chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2,openai_api_key=Config.OPENAI_API_KEY)

def retrieval(search: Search) -> List[Document]:
    return vectorstore.similarity_search(search.query)


sample_search = Search(query="what is camped on a cell ?")
retrieved_documents = retrieval(sample_search)





reference_list = ", ".join(doc.page_content for doc in retrieved_documents)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a 3GPP specialized assistant that answers to the user only based on the provided reference.If the answer can not be found in the given reference. respond "I could not find an answer." Here is the reference between brackets:[{reference_list}]."""
        ),
     
    ]
)


chain = prompt|chat

responses = chain.invoke(["what is camped on a cell ?"])
for response in responses:
    print("Generated Response:")
    print(response[1])