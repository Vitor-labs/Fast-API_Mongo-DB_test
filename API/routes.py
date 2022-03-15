from fastapi import APIRouter
from models import Item, ItemUpdate
from config import connect

itens_routes = APIRouter()

CONN_ERROR = {"error": "Connection error"}


# ==================== [READS] ====================
@itens_routes.get("/")
def get_all():
    conn = connect()
    if conn is None:
        return CONN_ERROR

    return conn.find({})


@itens_routes.get("/{item_name}")
def get_by_name(item_name: str):
    conn = connect()
    if conn is None:
        return CONN_ERROR

    return conn.find_one({"name": item_name})


@itens_routes.get("/{item_id}")
def get_item(item_id: int):
    conn = connect()
    if conn is None:
        return CONN_ERROR

    return conn.find_one({"id": item_id})
# ==================== [READS] ====================


# =================== [CREATES] ===================
@itens_routes.post("/")
def create_item(item: Item):
    conn = connect()
    if conn is None:
        return CONN_ERROR

    item_id = conn.count() + 1
    item.id = item_id
    conn.insert_one(item.dict())

    return {"message": f"Item {item.name} created with id {item_id}"}
# =================== [CREATES] ===================


# =================== [UPDATES] ===================
@itens_routes.put("/{item_id}")
def update_item(item_id: int, item: ItemUpdate):
    conn = connect()
    if conn is None:
        return CONN_ERROR

    conn.update_one({"id": item_id}, {"$set": item.dict()})
    return {"message": "Item {item_id} updated"}


@itens_routes.post("/{item_name}")
def update_by_name(name: str, item: Item):
    conn = connect()
    if conn is None:
        return CONN_ERROR

    conn.update_one({"name": name}, {"$set": item.dict()})
    return {"message": "Item {name} updated"}

@itens_routes.patch("/{item_id}")
def update_item_partial(item_id: int, item: ItemUpdate):
    conn = connect()
    if conn is None:
        return CONN_ERROR

    if item.name:
        conn.update_one({"id": item_id}, {"$set": {"name": item.name}})
    if item.color:
        conn.update_one({"id": item_id}, {"$set": {"color": item.color}})
    if item.price:
        conn.update_one({"id": item_id}, {"$set": {"price": item.price}})
    if item.quantity:
        conn.update_one({"id": item_id}, {"$set": {"quantity": item.quantity}})
    if item.is_offer:
        conn.update_one({"id": item_id}, {"$set": {"is_offer": item.is_offer}})

    return {"message": "Item {item_id} updated"}
# =================== [UPDATES] ===================


# =================== [DELETES] ===================
@itens_routes.delete("/{item_id}")
def delete_item(item_id: int):
    conn = connect()
    if conn is None:
        return CONN_ERROR

    conn.delete_one({"id": item_id})
    return {"message": f"Item {item_id} deleted"}


@itens_routes.delete("/{item_name}")
def delete_by_name(item_name: str):
    conn = connect()
    if conn is None:
        return CONN_ERROR

    conn.delete_one({"name": item_name})
    return {"message": f"Item {item_name} deleted"}
# =================== [DELETES] ===================
