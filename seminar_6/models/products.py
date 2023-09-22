from pydantic import BaseModel, Field


class ProductIn(BaseModel):
    name: str
    description: str = Field(max_length=256)
    price: int


class Product(BaseModel):
    id: int
    name: str
    description: str = Field(max_length=256)
    price: int
