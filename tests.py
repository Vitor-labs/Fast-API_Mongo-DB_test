from API.config import connect
from API.models import Item, ItemUpdate
import requests

BASE = "http://127.0.0.1:8000/itens/"
collection = None


def test_connection():
    response = requests.get(BASE)
    assert response.status_code == 200

    try:
        global collection
        collection = connect()
        assert collection is not None

        response = requests.get(BASE + "itens")
        assert response.status_code == 200
        print(response.status_code + response.json())

    except Exception as e:
        print(str(e))


def test_post():
    try:
        response = requests.post(
            BASE + "itens", json={"id": 7, "name": "Teste", "color": "red", "price": 1.99, "quantity": 1, "is_offer": False})

        print(response.status_code + response.json())

    except Exception as e:
        print(str(e))


def test_read():
    try:
        # Read All Items
        response = requests.get(BASE)
        assert response.status_code == 200
        print(response.status_code + response.json())

        # Read Item by Name
        response = requests.get(BASE + "Teste")
        assert response.status_code == 200
        print(response.status_code + response.json())

        # Read Item by ID
        response = requests.get(BASE + "1")
        assert response.status_code == 200
        print(response.status_code + response.json())

    except Exception as e:
        print(str(e))


def test_update():
    try:
        # Update Item by ID
        response = requests.put(BASE + "itens/1", json={"id": 3,
                                "name": "Teste", "color": "red", "price": 1.99, "quantity": 1, "is_offer": False})
        print(response.status_code + response.json())

        # Update Item by Name
        response = requests.put(BASE + "itens/Test", json={"id": 4,
                                "name": "Teste", "color": "red", "price": 1.99, "quantity": 1, "is_offer": False})
        print(response.status_code + response.json())

        # Update Partial
        response = requests.put(
            BASE + "itens/1", json={"id": 5, "quantity": 75, "is_offer": True})
        print(response.status_code + response.json())

    except Exception as e:
        print(str(e))


def test_delete():
    try:
        # Delete Item by ID
        response = requests.delete(BASE + "itens/0")
        print(response.status_code + response.json())

        # Delete Item by Name
        response = requests.delete(BASE + "itens/Test")
        print(response.status_code + response.json())

    except Exception as e:
        print("ERROR: " + str(e))


# test_read()
test_post()
