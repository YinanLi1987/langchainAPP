import uuid
from typing import Dict, List, Union
from examples import examples
from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    SystemMessage,
    ToolMessage,
)

from query_optimise import SubQuery



def tool_example_to_messages(example: Union[Dict, SubQuery])  -> List[BaseMessage]:
    messages: List[BaseMessage] = []
  
    #for tool_call in example["tool_calls"]:
    if isinstance(example, SubQuery):
            # Handle SubQuery objects
        messages.append(HumanMessage(content=example.sub_query))
    else:
            # Handle other types of examples
        messages.append(HumanMessage(content=example["input"]))
          
    openai_tool_calls = []

    tool_name = example.__class__.__name__

    if isinstance(example, SubQuery):
        tool_call_json = {"sub_query": example.sub_query}
    else:
        tool_call_json = example.json()

    openai_tool_calls.append(
            {
                "id": str(uuid.uuid4()),
                "type": "function",
                "function": {
                    "name": tool_name,
                    "arguments": tool_call_json,
                },
            }
        )
    messages.append(
        AIMessage(content="", additional_kwargs={"tool_calls": openai_tool_calls})
    )
    tool_outputs = getattr(example,"tool_outputs",None) 
    
    if tool_outputs is None:
        tool_outputs=[
        "This is an example of a correct usage of this tool. Make sure to continue using the tool this way."
    ] * len(openai_tool_calls)
    for output, tool_call in zip(tool_outputs, openai_tool_calls):
        messages.append(ToolMessage(content=output, tool_call_id=tool_call["id"]))
    return messages


example_msgs = [msg for ex in examples for msg in tool_example_to_messages(ex)]