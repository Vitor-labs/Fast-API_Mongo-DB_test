from pymongo import MongoClient

# ============== [CONSTANTS] ==============
MONGO_DB_NAME = "myFirstDatabase"
MONGO_COLLECTION_NAME = "Tests"

MONGO_USER = "m001-student"
MONGO_PASSWORD = "m001-mongodb-basics"
MONGO_URI = f'mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@sandbox.iwqks.mongodb.net/{MONGO_DB_NAME}?retryWrites=true&w=majority'
# ========================================


def connect() -> MongoClient:
    """
    Try to Connect to MongoDB
    """
    try:
        client = MongoClient(MONGO_URI)
        assert client is not None
        print(f"Connected to MongoDB at {MONGO_URI}")

        db = client[MONGO_DB_NAME]
        collection = db[MONGO_COLLECTION_NAME]

        return collection

    except Exception as e:
        print("ERROR: " + str(e))
        return None


connect()
