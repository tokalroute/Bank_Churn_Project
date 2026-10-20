from typing import Literal
from pydantic import BaseModel, Field

class Customer(BaseModel):
    credit_score: int = Field(ge=350, le=850)
    geography: Literal["France", "Germany", "Spain"]
    age: int = Field(ge=18, le=100)
    tenure: int = Field(ge=0, le=10)
    balance: float = Field(ge=0)
    num_of_products: int = Field(ge=1, le=4)
    has_credit_card: bool
    is_active_member: bool


# feature_selection --> filter method , wrapper method , embeeded method 