from .connection import ConnES
from uuid import uuid4
from elasticsearch.helpers import bulk
from logger import Logger
import logging

try:
    logger = Logger.get_logger()
except Exception as e:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
class Crud:
    def __init__(self, index_name):
        self.es = ConnES.get_instance().connect()
        self.index_name = index_name


    def insert_data(self, data):
        """
        Insert a single document into Elasticsearch.
        :param data:
        :return:
        """
        try:
            res = self.es.index(index=self.index_name, document=data)
            logger.info("Data inserted successfully.")
            return res
        except Exception as e:
            logger.error(f"Failed to insert data: {e}")

    def insert_data_bulk(self, data):
        """
        Insert a pandas DataFrame into Elasticsearch using bulk API.
        Each row becomes a document.
        """
        data = data.to_dict(orient='records')
        try:
            actions = \
            [
                {
                    "_index": self.index_name,
                    "_id" :str(uuid4()),
                    "_source": doc
                }
                for doc in data
            ]
            res = bulk(self.es,actions)
            logger.info(f"Bulk inserted successfully. Inserted {res[0]} documents.")

        except Exception as e:
            logger.error(f"Failed to insert data: {e}")

    def update_data(self, doc_id, data):
        """
        Update a document in Elasticsearch.
        :param doc_id:
        :param data:
        :return:
        """
        try:
            res = self.es.update(index=self.index_name, id=doc_id, body={"doc": data})
            logger.info("Data updated successfully.")
            return res
        except Exception as e:
            logger.error(f"Failed to update data: {e}")

    def delete_data(self, doc_id):
        """
        Delete a document from Elasticsearch.
        :param doc_id:
        :return:
        """
        try:
            res = self.es.delete(index=self.index_name, id=doc_id)
            logger.info("Data deleted successfully.")
            return res
        except Exception as e:
            logger.error(f"Failed to delete data: {e}")

    def search_data(self, query):
        """
        Search for documents in Elasticsearch.
        :param query:
        :return:
        """
        try:
            res = self.es.search(index=self.index_name, body=query)
            logger.info("Data searched successfully.")
            return res
        except Exception as e:
            logger.error(f"Failed to search data: {e}")
