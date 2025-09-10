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

    #READ ALL
    #find all files end with .wav

    def find_all_documents(self):
        data = self.fs.find({"filename": re.compile(".*\.wav$")})
        print(data)
        return data

    def get_all_hash_keys(self):
        data = self.collection.find()
        print(data)
        return [doc["hash"] for doc in data]

    def get_document_by_hash(self, hash_value: str):
        data = self.fs.find_one({"hash": hash_value})
        print(data)
        return data

    def download_file(self, doc_id: str, target_path: Path):
        doc = self.get_document_by_id(doc_id)
        if not doc:
            logger.error("doc not found")
            raise FileNotFoundError("doc not found")

        if doc.get("storage_type") == "binary":
            with open(target_path, "wb") as out:
                out.write(doc["file_data"])
        elif doc.get("storage_type") == "gridfs":
            grid_out = self.fs.get(doc["gridfs_id"])
            with open(target_path, "wb") as out:
                out.write(grid_out.read())
        else:
            logger.error("storage type not found")
            raise ValueError("storage type not found")

    # UPDATE
    def update_document(self, doc_id: str, update_data: dict) -> bool:
        result = self.collection.update_one(
            {"_id": ObjectId(doc_id)},
            {"$set": update_data}
        )
        return result.modified_count > 0

    # DELETE
    def delete_document(self, doc_id: str) -> bool:
        """if hash not found return false"""
        doc = self.get_document_by_id(doc_id)
        if not doc:
            return False

        if doc.get("storage_type") == "gridfs":
            self.fs.delete(doc["gridfs_id"])

        result = self.collection.delete_one({"_id": ObjectId(doc_id)})
        return result.deleted_count > 0

    def close_connection(self):
        self.conn.close()
        logger.info("MongoCRUD connection closed.")