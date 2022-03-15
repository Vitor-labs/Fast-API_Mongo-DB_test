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


test_connection()
