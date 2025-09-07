import os
from dotenv import load_dotenv
from pathlib import Path
from metadataExtractor import MetadataExtractor
from kafka_objects.producer import Producer
from kafka_objects.consumer import Consumer


load_dotenv()
AUODIO_FOLDER = Path(os.getenv("AUDIO_FOLDER"))
class LoadDataprocess:
    def __init__(self, path):
        self.path = Path(path)
        self.files = self.path.iterdir()
        self.products = []
        self.producer = Producer()
        self.load_metadata()
        self.publish_metadata()

    def load_metadata(self):
        for file in self.files:
            if file.is_file():
                self.products.append(MetadataExtractor.extract_metadata(file))

    def publish_metadata(self):
        print("Publishing metadata...")
        for product in self.products:
            self.producer.publish_message("metadata", product)
            print(f"Published metadata for {product['filename']}")



if __name__ == "__main__":
    loadDataprocess = LoadDataprocess(AUODIO_FOLDER)

    #check if the metadata is published
    consumer = Consumer(["metadata"])
    for message in consumer.get_consumer():
        print(message)
