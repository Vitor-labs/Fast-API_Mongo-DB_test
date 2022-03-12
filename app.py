from fastapi import FastAPI, Path, HTTPException, status
from typing import Optional
from pydantic import BaseModel

# ============== CONSTANTS ==============
NOT_FOUND_MSG = "Item specified not found"


class Item(BaseModel):
    Name: str
    Price: float
    is_offer: bool = True
    quantity: int = 1
    color: Optional[str] = None


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    Price: Optional[float] = None
    is_offer: Optional[bool] = None
    quantity: Optional[int] = None
    color: Optional[str] = None


app = FastAPI()

inventory = {}


@app.get('/')
def index():
    return {"message": "Hello World Test"}


@app.get("/about")
def about():
    return {"message": "This is a Test for a future project"}


@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None,
                                 description="ID of the item to return",
                                 title="Item ID", gt=0)):
    return inventory.get(item_id)


@app.get("/get-item-by-name")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


@app.get("/get-all-items")
def get_all_items():
    return inventory


@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id in inventory:
        if item.name != None:
            inventory[item_id].name = item.name
        if item.Price != None:
            inventory[item_id].Price = item.Price
        if item.is_offer != None:
            inventory[item_id].is_offer = item.is_offer
        if item.quantity != None:
            inventory[item_id].quantity = item.quantity
        if item.color != None:
            inventory[item_id].color = item.color

        return inventory[item_id]
    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)


@app.post("/add-item")
def add_item(item: Item):
    item_id = max(inventory.keys()) + 1
    inventory[item_id] = item
    return inventory[item_id]


@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
    if item_id in inventory:
        del inventory[item_id]
        return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail=NOT_FOUND_MSG)
