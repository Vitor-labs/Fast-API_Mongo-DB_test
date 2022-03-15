import collections
from API.config import connect
import requests

BASE = "http://127.0.0.1:8000/"
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
    except Exception as e:
        print("ERROR: " + str(e))


def test_post():
    try:
        global collection
        if collection is None:
            collection = connect()

        response = requests.post(
            BASE + "itens", json={"name": "Teste", "color": "red", "price": 1.99, "quantity": 1, "is_offer": False})

        assert response.status_code == 201
        assert response.json()["item_id"] is not None

        print(response.json())

    except Exception as e:
        print("ERROR: " + str(e))


test_post()
