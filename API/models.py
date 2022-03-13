from typing import Optional
from pydantic import BaseModel
from pymongo import MongoClient

# ============== [CONSTANTS] ==============
MONGO_DB_NAME = "Tests"
MONGO_COLLECTION_NAME = "items"

MONGO_USER = "m001-student"
MONGO_PASSWORD = "m001-mongodb-basics"
DB_URL = "mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@sandbox.iwqks.mongodb.net/{MONGO_DB_NAME}?retryWrites=true&w=majority"

client = MongoClient(DB_URL, 27017)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]
# ========================================


class Item(BaseModel):
    _id: int = 0
    name: str = "None"
    price: float = 0.0
    is_offer: bool = False
    quantity: int = 0
    color: Optional[str] = None

    def __init__(self, name: str, price: float, quantity: int, color: Optional[str]):
        self.name = name
        self.price = price
        self.is_offer = True if price > 100 else quantity > 0
        self.quantity = quantity
        self.color = color

    def info(self) -> str:
        return f"Item [{self._id}]: {self.name} | Price: ${self.price} | Quantity: {self.quantity} | Color: {self.color}"

    def is_on_sale(self) -> str:
        if not self.is_offer:
            return f"Item {self.name} is not out of stock"
        elif self.color is not None:
            return f"Item {self.name} of color {self.color} has {self.quantity} in stock and costs ${self.price}"
        else:
            return f"Item {self.name} has {self.quantity} in stock and costs ${self.price}"

    def dict(self) -> dict:
        return {
            "Name": self.name,
            "Price": self.price,
            "is_offer": self.is_offer,
            "quantity": self.quantity,
            "color": self.color
        }


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    Price: Optional[float] = None
    is_offer: Optional[bool] = None
    quantity: Optional[int] = None
    color: Optional[str] = None
