from pymongo import MongoClient
from utils.logger import Logger
import logging

try:
    logger = Logger.get_logger()
except Exception as e:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

class MongoConnection:
    def __init__(self, uri: str, db_name: str, collection_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        logger.info(f"MongoDB connection initialized. DB: {db_name}, Collection: {collection_name}")
    def get_collection(self):
        return self.collection

    def close(self):
        self.client.close()
        logger.info("MongoDB connection closed.")