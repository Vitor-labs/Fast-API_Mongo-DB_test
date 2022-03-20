from models import Item, ItemUpdate


def serial_item(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "color": item["color"],
        "price": item["price"],
        "quantity": item["quantity"],
        "is_offer": item["is_offer"]
    }


def serial_items(items) -> list:
    return [serial_item(item) for item in items]


def serial_item_update(item: ItemUpdate) -> dict:
    return {
        "name": item["name"],
        "color": item["color"],
        "price": item["price"],
        "quantity": item["quantity"],
        "is_offer": item["is_offer"]
    }


def serial_items_update(items: list) -> list:
    return [serial_item_update(item) for item in items]
