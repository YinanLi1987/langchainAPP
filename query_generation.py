from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from query_schema import Search
from settings import Config
from typing import List
from langchain_core.documents import Document
from indexing_document import vectorstore


system = """You are an expert at converting user questions into database queries. \
You have access to a database of 3GPP specifications:38.307,38.306,38.305,38.304,38.300. \
Given a question, return a list of database queries optimized to retrieve the most relevant results.

If there are acronyms or words you are not familiar with, do not try to rephrase them."""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0,openai_api_key=Config.OPENAI_API_KEY)
structured_llm = llm.with_structured_output(Search)

def retrieval(search: Search) -> List[Document]:
    #if search.publish_year is not None:
        # This is syntax specific to Chroma,
        # the vector database we are using.
      #  _filter = {"publish_year": {"$eq": search.publish_year}}
    #else:
       # _filter = None
    return vectorstore.similarity_search(search.query)
query_analyzer = {"question": RunnablePassthrough()} | prompt | structured_llm

retrieval_chain = query_analyzer | retrieval




results = retrieval_chain.invoke(" what is camped on a cell ?")
if results:
    most_relevant_doc = results[0]  # Get the most relevant document
    print("Most Relevant Document Content:")
    print(most_relevant_doc.page_content)  # Print the content of the most relevant document
    print("-" * 50)  # Add a separator for clarity
else:
    print("No relevant documents found.")