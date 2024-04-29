from langchain_openai import ChatOpenAI
from settings import Config
from langchain_core.prompts import ChatPromptTemplate
from typing import List
from langchain_core.documents import Document
from indexing_document import vectorstore
from query_schema import Search
from langchain_core.runnables import RunnablePassthrough
system = """You are an expert at converting user questions into database queries. \You have access to a database of CR documents. \Given a question, return a list of database queries optimized to retrieve the most relevant results.If there are acronyms or words you are not familiar with, do not try to rephrase them."""
#Define the LLM model 
chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2,openai_api_key=Config.OPENAI_API_KEY)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system",system),
        ("human","{question}"),
     
    ]
)
structured_chat=chat.with_structured_output(Search)
query_analyzer = {"question": RunnablePassthrough()} | prompt | structured_chat


#Define retrieval method and store retrivaled data into a list 
def retrieval(search:Search) -> List[Document]:
    if search.Source_to_WG is not None:
       #This is sytax specific to Chroma,
       #the vector database we are using
       _filter={"Source_to_WG":{"$eq":search.Source_to_WG}}
    else:
        _filter=None
       
    return vectorstore.similarity_search(search.query,filter=_filter )
retrieval_chain=query_analyzer | retrieval
retrieved_documents = retrieval_chain.invoke("which cr source_to_WG is MediaTek Inc.?")
#reference_list = ", ".join(doc.page_content for doc in retrieved_documents)



for response in retrieved_documents:
    print("Generated Response:")
    print(response)
   
