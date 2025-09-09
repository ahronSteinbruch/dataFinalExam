from kafka_objects.consumer import Consumer
from getHashForFile import get_file_hash
from pathlib import Path
from threading import Thread
from config import Config
from ElasticUploader import ElasticUploader
from MongoUploader import MongoUploader

TOPIC = "metadata"
class DataLoad:
    def __init__(self):
        self.consumer = Consumer([Config.KAFKA_TOPIC])
        self.elastic = ElasticUploader(Config.ELASTIC_HOST, Config.ELASTIC_INDEX)
        self.mongo = MongoUploader(Config.MONGO_URI, Config.MONGO_DB, Config.MONGO_FS_COLLECTION)

    def add_hash_key(self, data):
        data["hash"] = get_file_hash(data["path"])
        return data

    def load_data(self):
        con = self.consumer.get_consumer()
        for doc in con:
            print(doc.value)
            data = self.add_hash_key(doc.value)
            self.process_doc(data)

    def process_doc(self, doc: dict):
        file_path = Path(doc["path"])
        file_hash = doc["hash"]


        # Thread 1 for mongo
        mongo_thread = Thread(
            target=self.mongo.upload_file,
            args=(file_path, file_hash)
        )

        # Thread 2 for elasticsearch
        elastic_thread = Thread(
            target=self.elastic.upload_metadata,
            args=(doc,)
        )

        mongo_thread.start()
        elastic_thread.start()

        mongo_thread.join()
        elastic_thread.join()




if __name__ == "__main__":
    dataLoad = DataLoad()
    dataLoad.load_data()
