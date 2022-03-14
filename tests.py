import requests
import json

BASE = "http://127.0.0.1:8000/"


def test_create_item():
    item = {
        "name": "Test",
        "price": 10.0,
        "quantity": 10,
        "color": "Blue"
    }
    try:
        response = requests.post(BASE + "add-item", json=item)
        print(response.status_code)
        print(response.text)

    except Exception as e:
        print(e)


def test_read_item():
    try:
        response = requests.get(BASE + "get-item/1")
        print(response.status_code)
        print(response.text)

    except Exception as e:
        print(e)
