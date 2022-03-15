from pymongo import MongoClient

# ============== [CONSTANTS] ==============
MONGO_DB_NAME = "Tests"
MONGO_COLLECTION_NAME = "Itens_Store"

MONGO_USER = "m001-student"
MONGO_PASSWORD = "m001-mongodb-basics"
MONGO_URL = "mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@sandbox.iwqks.mongodb.net/{MONGO_DB_NAME}?retryWrites=true&w=majority"
# ========================================


def connect():
    """
    Try to Connect to MongoDB
    """
    try:
        client = MongoClient(MONGO_URL, 27017, serverSelectionTimeoutMS=1000)
        client.server_info()

        db = client[MONGO_DB_NAME]
        collection = db[MONGO_COLLECTION_NAME]
    except Exception as e:
        print("ERROR: " + str(e))
        return None

    return collection
