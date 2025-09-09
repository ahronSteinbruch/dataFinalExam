import os
from dotenv import load_dotenv
from pathlib import Path

from config import Config
from metadataExtractor import MetadataExtractor
from kafka_objects.producer import Producer
from logger import Logger
import logging

try:
    logger = Logger.get_logger()
except Exception as e:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

load_dotenv()
AUODIO_FOLDER = Path(Config.AUDIO_FOLDER)
class LoadDataprocess:
    def __init__(self, path):
        self.path = Path(path)
        self.files = self.path.iterdir()
        self.products = []
        self.producer = Producer()
        self.load_metadata()
        self.publish_metadata()
        logger.info("LoadDataprocess initialized.")

    def load_metadata(self):
        for file in self.files:
            if file.is_file():
                self.products.append(MetadataExtractor.extract_metadata(file))
                logger.info(f"Loaded metadata for {file.name}")

    def publish_metadata(self):
        logger.info("Publishing metadata...")
        for product in self.products:
            self.producer.publish_message("metadata", product)
            logger.info(f"Published metadata for {product['filename']}")



if __name__ == "__main__":
    loadDataprocess = LoadDataprocess(Config.AUDIO_FOLDER)


