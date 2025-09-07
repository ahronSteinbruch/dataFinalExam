import Elastic_service
from kafka_objects.consumer import Consumer
from getHashForFile import get_file_hash

TOPIC = "metadata"
class DataLoad:
    def __init__(self):
        self.index_name = "aodio_files"
        self.es = Elastic_service.ConnES().get_instance().connect()
        self.consumer = Consumer(["metadata"])
        self.dal = Elastic_service.DAL(self.index_name)

    def add_hash_key(self, data):
        data["hash"] = get_file_hash(data["path"])
        return data

    def load_data(self):
        self.consumer.subscribe(TOPIC)
        for message in self.consumer:
            data = self.add_hash_key(message.value)
            insertToElastic(data)
            insertToMongo(data)
            print(f"Data loaded successfully to elasticsearch: {data}")




