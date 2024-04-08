from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain.output_parsers import PydanticToolsParser
from langchain_openai import ChatOpenAI
from query_optimise import Search 
from query_optimise import SubQuery
from settings import Config
from typing import List
from langchain_core.documents import Document
from indexing_document import vectorstore
from langchain_core.prompts import MessagesPlaceholder
from tool_example_to_messages import example_msgs
system = """You are an expert at converting user questions into database queries. \
You have access to a database of 3GPP specifications:38.307,38.306,38.305,38.304,38.300. \
Given a question, return a list of database queries optimized to retrieve the most relevant results.

Perform query decomposition. Given a user question, break it down into the most specific sub questions you can \
which will help you answer the original question. Each sub question should be about a single concept/fact/idea.

If there are acronyms or words you are not familiar with, do not try to rephrase them."""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        MessagesPlaceholder("examples", optional=True),
        ("human", "{question}"),
    ]
)
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0,openai_api_key=Config.OPENAI_API_KEY)
llm_with_tools = llm.bind_tools([SubQuery])
parser = PydanticToolsParser(tools=[SubQuery])
#structured_llm = llm.with_structured_output(Search)

#def retrieval(search: Search) -> List[Document]:
    #if search.publish_year is not None:
        # This is syntax specific to Chroma,
        # the vector database we are using.
      #  _filter = {"publish_year": {"$eq": search.publish_year}}
    #else:
       # _filter = None
    #return vectorstore.similarity_search(search.query)
#query_analyzer = {"question": RunnablePassthrough()} | prompt | llm_with_tools | parser| structured_llm

#retrieval_chain = query_analyzer | retrieval
query_analyzer = prompt.partial(examples=example_msgs)  | llm_with_tools | parser

parsed_results = query_analyzer.invoke({"question": "in the context of radio technology, what is camped on a cell and how to make it work ?"})

for result in parsed_results:
    if isinstance(result, SubQuery):
        print("SubQuery:", result.sub_query)
    elif isinstance(result,str):
        print("Answer:",result)
#results = retrieval_chain.invoke("in the context of radio technology, what is camped on a cell ?")
#if results:
 #   most_relevant_doc = results[0]  # Get the most relevant document
  #  print("Most Relevant Document Content:")
   # print(most_relevant_doc.page_content)  # Print the content of the most relevant document
    #print("-" * 50)  # Add a separator for clarity
#else:
 #   print("No relevant documents found.")