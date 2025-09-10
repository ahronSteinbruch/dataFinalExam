from bson.objectid import ObjectId
from pathlib import Path
from gridfs import GridFS
from .conection import MongoConnection
from utils.logger import Logger
import logging
import re
try:
    logger = Logger.get_logger()
except Exception as e:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
class MongoCRUD:
    def __init__(self, uri: str,db_name: str, collection_name: str):
        self.conn = MongoConnection(uri, db_name, collection_name)
        self.collection = self.conn.get_collection()
        self.fs = GridFS(self.conn.db)
        logger.info("MongoCRUD initialized.")

    # CREATE
    def insert_file(self, file_path: Path, hash_value: str) -> str:
        file_size = file_path.stat().st_size


        with open(file_path, "rb") as f:
            gridfs_id = self.fs.put(f,_id=hash_value, filename=file_path.name,hash=hash_value)
            logger.info("File inserted successfully.")
        return gridfs_id

    # READ
    def get_document_by_id(self, doc_id: str) -> dict | None:
        return self.fs.find_one({"_id": ObjectId(doc_id)})


    def get_document_by_hash(self, hash_value: str):
        data = self.fs.find_one({"hash": hash_value})
        return data


    def close_connection(self):
        self.conn.close()
        logger.info("MongoCRUD connection closed.")