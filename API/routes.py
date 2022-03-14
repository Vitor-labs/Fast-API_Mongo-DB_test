from fastapi import APIRouter
from models import Item, ItemUpdate

itens_routes = APIRouter()


@itens_routes.get("/")
def get_items():
    return [
        Item(name="Item 1", color="Red", price=10.0, quantity=2, is_offer=True),
        Item(name="Item 2", color="Blue", price=20.0, quantity=3, is_offer=False),
        Item(name="Item 3", color="Green",
             price=30.0, quantity=4, is_offer=True),
    ]


@itens_routes.get("/{item_id}")
def get_item(item_id: int):
    return Item(name="Item 1", color="Red", price=10.0, quantity=2, is_offer=True)


@itens_routes.post("/")
def create_item(item: Item):
    return item


@itens_routes.put("/{item_id}")
def update_item(item_id: int, item: ItemUpdate):
    return {"message": "Item updated"}


@itens_routes.delete("/{item_id}")
def delete_item(item_id: int):
    return {"message": "Item deleted"}
