from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from settings import Config
from typing import List
from langchain_core.documents import Document
from indexing_document import vectorstore



system = """You are an expert at converting user questions into database queries. \
You have access to a database of 3GPP specifications and change request document. \
Given a question, return a list of database queries optimized to retrieve the most relevant results.

If there are acronyms or words you are not familiar with, do not try to rephrase them."""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)
#llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2,openai_api_key=Config.OPENAI_API_KEY)

userinput="which CR is from Mediatek?"
def retrieval(userinput) -> List[Document]:
   return vectorstore.similarity_search("which CR is from Mediatek?")
#query_analyzer = {"question": RunnablePassthrough()} | prompt | structured_llm

retrieval_chain = {"question": RunnablePassthrough()} |  prompt | retrieval
#retrieval_chain = query_analyzer | retrieval


results = retrieval_chain.invoke({"question": userinput})
if results:
    most_relevant_doc = results[0]  # Get the most relevant document
    print("Most Relevant Document Content:")
    print(most_relevant_doc.page_content)  # Print the content of the most relevant document
    print("-" * 50)  # Add a separator for clarity
else:
    print("No relevant documents found.")
