from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    id: Optional[int]
    name: str
    color: str
    price: float
    quantity: int
    is_offer: bool

    def info(self):
        print(f"{self.name} is {self.color} and costs {self.price}")


class ItemUpdate(BaseModel):
    name: Optional[str]
    color: Optional[str]
    price: Optional[float]
    quantity: Optional[int]
    is_offer: Optional[bool]
