from fastapi import APIRouter
from bson.objectid import ObjectId
# ====================== [INSIDE INPORTS] =========================
from models import Item, ItemUpdate
from config import connect
from util import serial_item, serial_items, serial_item_update
# ====================== [INSIDE INPORTS] =========================
itens_routes = APIRouter()


CONN_ERROR = {"error": "Connection error"}
CREATE_ERROR = {"error": "Create error"}
READ_ERROR = {"error": "Read error"}
UPDATE_ERROR = {"error": "Update error"}
DELETE_ERROR = {"error": "Delete error"}


# =================== [CREATES] ===================
@itens_routes.post("/")
async def create_item(item: Item):  # Tested OK
    conn = connect()
    if conn is None:
        return CONN_ERROR

    try:
        _id = conn.insert_one(dict(item))
        data = serial_items(conn.find({"_id": _id.inserted_id}))
        return {"Status": "OK", "item": data}

    except Exception as e:
        print(e)
        return CREATE_ERROR
# =================== [CREATES] ===================


# ==================== [READS] ====================
@itens_routes.get("/")
async def get_all():  # Tested OK
    conn = connect()
    if conn is None:
        return CONN_ERROR

    try:
        items = conn.find()
        return {"Status": "OK", "Items": serial_items(items)}

    except Exception as e:
        print(e)
        return READ_ERROR


@itens_routes.get("/{item_name}")
async def get_by_name(item_name: str):  # Tested OK
    conn = connect()
    if conn is None:
        return CONN_ERROR

    try:
        items = conn.find({"name": item_name})
        if items is None:
            return {"Status": "OK", "Items": "No item found"}
        return {"Status": "OK", "Items": serial_items(items)}
    except Exception as e:
        print(e)
        return READ_ERROR


@itens_routes.get("/{item_id}")
async def get_item(item_id: str):  # Tested No Return
    conn = connect()
    if conn is None:
        return CONN_ERROR

    try:
        item = serial_item(conn.find_one({"_id": ObjectId(item_id)}))
        if item is None:
            return {"Status": "Error", "Error": "Item not found"}
        return {"Status": "OK", "Item": item}
    except Exception as e:
        print(e)
        return READ_ERROR
# ==================== [READS] ====================


# =================== [UPDATES] ===================
@itens_routes.put("/{item_id}")
async def update_item(item_id: str, item: ItemUpdate):  # Tested OK
    conn = connect()
    if conn is None:
        return CONN_ERROR

    try:
        conn.update_one({"_id": ObjectId(item_id)}, {"$set": dict(item)})
        item = serial_item_update(conn.find_one({"_id": ObjectId(item_id)}))
        return {"Status": "OK", "Item": item}

    except Exception as e:
        print(e)
        return UPDATE_ERROR


@itens_routes.put("/{item_name}")
async def update_by_name(name: str, item: ItemUpdate):  # Tested Fail in $set
    conn = connect()
    if conn is None:
        return CONN_ERROR

    try:
        query = {"name": name}
        new_values = {"$set": dict(item)}
        conn.update_many(query, new_values)
        item = serial_item(conn.find_one({"name": name}))
        return {"Status": "OK", "Item": item}

    except Exception as e:
        print(e)
        return UPDATE_ERROR
# =================== [UPDATES] ===================


# =================== [DELETES] ===================
@itens_routes.delete("/{item_id}")
def delete_item(item_id: str):  # Tested OK
    conn = connect()
    if conn is None:
        return CONN_ERROR

    try:
        conn.delete_one({"_id": ObjectId(item_id)})
        return {"Status": "OK"}

    except Exception as e:
        print(e)
        return DELETE_ERROR


@itens_routes.delete("/{item_name}")
def delete_by_name(item_name: str):  # Tested Erro on valid objectid, same as update
    conn = connect()
    if conn is None:
        return CONN_ERROR

    try:
        conn.delete_one({"name": item_name})
        return {"Status": "OK"}

    except Exception as e:
        print(e)
        return DELETE_ERROR
# =================== [DELETES] ===================
