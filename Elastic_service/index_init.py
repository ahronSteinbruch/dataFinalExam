from .connection import ConnES
from logger import Logger
import logging

try:
    logger = Logger.get_logger()
except Exception as e:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
class Index_init:
    def __init__(self,index_name,mapping=None):
        self.es = ConnES.get_instance().connect()
        self.index_name = index_name
        self.create_index()
        # if mapping is None:
        #     self.create_mapping(mapping)

    def create_index(self):
        if not self.es.indices.exists(index=self.index_name):
            try:
                self.es.indices.create(index=self.index_name)
                logger.info(f"Index {self.index_name} created successfully.")
            except Exception as e:
                logger.error(f"Failed to create index {self.index_name}: {e}")

    def create_mapping(self,mapping):
        try:
            self.es.indices.put_mapping(index=self.index_name, body=mapping)

        except Exception as e:
            logger.error(f"Failed to create mapping for index {self.index_name}: {e}")

    def delete_index(self):
        try:
            self.es.indices.delete(index=self.index_name, ignore_unavailable=True)
            logger.info(f"Index {self.index_name} deleted successfully.")
        except Exception as e:
            logger.error(f"Failed to delete index {self.index_name}: {e}")
