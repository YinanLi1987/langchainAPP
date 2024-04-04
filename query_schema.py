from typing import Optional

from langchain_core.pydantic_v1 import BaseModel, Field


class Search(BaseModel):
    """Search over a database of 3GPP specifications:38.307,38.306,38.305,38.304,38.300 ."""

    query: str = Field(
        ...,
        description="Similarity search query applied to 3GPP specifications:38.307,38.306,38.305,38.304,38.300.",
    )
    # publish_year: Optional[int] = Field(None, description="Year video was published")