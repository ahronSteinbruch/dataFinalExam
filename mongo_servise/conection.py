from pymongo import MongoClient

class MongoConnection:
    def __init__(self, uri: str, db_name: str, collection_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def get_collection(self):
        return self.collection

    def close(self):
        self.client.close()