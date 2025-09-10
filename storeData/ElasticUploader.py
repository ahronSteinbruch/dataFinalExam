from utils.Elastic_service.DAL import DAL
from utils.logger import Logger
import logging

try:
    logger = Logger.get_logger()
except Exception as e:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
class ElasticUploader:
    def __init__(self, host, index):
        self.dal = DAL(index,create_index=True)
        logger.info(f"ElasticUploader initialized for index {index}")
    def upload_metadata(self, metadata):
        self.dal.insert_data(metadata)
        logger.info(f"Metadata uploaded to Elasticsearch successfully.")


