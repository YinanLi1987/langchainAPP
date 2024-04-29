from typing import Optional

from langchain_core.pydantic_v1 import BaseModel, Field


#metadata = {
#    "title0":"3GPP TS 38.213",
#    "title1": "Technical Specification Group Radio Access Network",
#    "title2":"NR",
#    "title3":"Physical layer procedures for control",
#    "Release": 18,
#    "Version":"V18.2.0",
#    "Publish_time":"2024-03",
#}


class Search(BaseModel):
    """Search over a database of 3GPP specifications:38.202,38.211,38.212,38.213,38.214,38.215"""

    query: str = Field(
        ...,
        description="Similarity search query applied to 3GPP specifications or change request document CR",
    )
    
    Source_to_WG: str =Field(
        
        ..., 
        description="CR's source to WG")
    
    publish_year: Optional[int] = Field(
        None, 
        description="Year and month document was released")