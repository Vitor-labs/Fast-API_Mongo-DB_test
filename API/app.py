from fastapi import FastAPI
from models import Item, ItemUpdate
from fastapi import Path, HTTPException
from models import Item, ItemUpdate, collection


app = FastAPI()

CREATE_FAIL = "Failed to create item"
READ_FAIL = "Failed to read item"
UPDATE_FAIL = "Failed to update item"
DELETE_FAIL = "Failed to delete item"


@app.get('/')
def index() -> dict:
    return {"message": "[Fast API / Mongo DB] - Test"}


@app.get("/about")
def about() -> dict:
    return {"message": "This is a Test for a future project"}


# ====================== [CREATES] =======================
@app.post("/add-item")
def add_item(item: Item) -> bool:
    if collection.insert_one(item.dict()) is None:
        raise HTTPException(status_code=500, detail=CREATE_FAIL)

    return True
# ====================== [CREATES] =======================


# ======================= [READS] ========================
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None,
                                 description="ID of the item to return",
                                 title="Item ID", gt=0)) -> Item:

    item = collection.find_one({"_id": item_id})
    if item is None:
        raise HTTPException(status_code=404, detail=CREATE_FAIL)

    return Item(**item)


@app.get("/get-item-by-name")
def get_item(name: str) -> Item:
    item = collection.find_one({"name": name})
    if item is None:
        raise HTTPException(status_code=404, detail=CREATE_FAIL)

    return Item(**item)


@app.get("/get-all-items")
def get_all_items() -> dict:
    items = collection.find()
    return {
        "message": "All items",
        "items": [item for item in items]
    }
# ======================= [READS] ========================


# ====================== [UPDATES] =======================
@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: ItemUpdate) -> bool:
    item_to_update = collection.find_one({"_id": item_id})
    if item_to_update is None:
        raise HTTPException(status_code=404, detail=UPDATE_FAIL)

    collection.update_one({"_id": item_id}, {"$set": item.dict()})
    return True
# ====================== [UPDATES] =======================


# ====================== [DELETES] =======================
@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int) -> dict:
    item_to_delete = collection.find_one({"_id": item_id})
    if item_to_delete is None:
        raise HTTPException(status_code=404, detail=DELETE_FAIL)

    try:
        collection.delete_one({"_id": item_id})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    else:
        return {"message": f"Item {item_id} deleted"}


@app.get("/delete-by-name/{name}")
def delete_by_name(name: str) -> dict:
    items_to_delete = collection.find({"name": name})
    if items_to_delete.count() == 0:
        raise HTTPException(status_code=404, detail=DELETE_FAIL)

    try:
        collection.delete_many({"name": name})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    else:
        return {"message": f"{items_to_delete.count()} items with name {name} deleted"}


@app.delete("/delete-all")
def delete_all() -> dict:
    try:
        collection.delete_many({})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    else:
        return {"message": "All items deleted"}
# ====================== [DELETES] =======================
