from typing import List,Dict,Any
from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel,Field


class Summary(BaseModel):
    person:List[str] =Field(description="person")
    organisation: List[str] = Field(description="any organisation")
    transaction: List[str]=Field(description="type of transaction")
    def to_dict(self) -> Dict[str,Any]:
        return {"person": self.person,"organisation": self.organisation,"transaction":self.transaction}
summary_parser=PydanticOutputParser(pydantic_object=Summary)
