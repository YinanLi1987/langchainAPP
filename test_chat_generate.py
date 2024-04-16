from langchain_openai import ChatOpenAI
from settings import Config
from langchain_core.prompts import ChatPromptTemplate
from typing import List
from langchain_core.documents import Document
from indexing_document import vectorstore


#Define the LLM model 
chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2,openai_api_key=Config.OPENAI_API_KEY)
#Define retrieval method and store retrivaled data into a list 
def retrieval(userinput) -> List[Document]:
   return vectorstore.similarity_search("what is a snowboard ?")


# Define the retrivaled data list
retrieved_documents = retrieval("what is a snowboard ?")

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

responses = chain.invoke(["what is a snowboard ?"])
for response in responses:
    print("Generated Response:")
    print(response[1])