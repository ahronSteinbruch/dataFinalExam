import logging
from elasticsearch import Elasticsearch
from datetime import datetime
from config import Config
class Logger:
    """
    singleton logger class thet log to elasticsearch and console
    """
    _logger = None
    @classmethod
    def get_logger(
            cls,
            name="logy",
            es_host=Config.ELASTIC_HOST,
            index=Config.ELASTIC_LOG_INDEX,
            level=logging.DEBUG
    ):
        if cls._logger:
            return cls._logger
        logger = logging.getLogger(name)
        logger.setLevel(level)
        if not logger.handlers:
            es = Elasticsearch(es_host)
            class ESHandler(logging.Handler):
                def emit(self, record):
                    try:
                        es.index(index=index, document={
                        "timestamp": datetime.utcnow().isoformat(),
                        "level": record.levelname,
                        "logger": record.name,
                        "message": record.getMessage()
                        })
                    except Exception as e:
                        print(f"ES log failed: {e}")
            logger.addHandler(ESHandler())
            logger.addHandler(logging.StreamHandler())
        cls._logger = logger
        return logger

#use it like this
logger = Logger.get_logger()
logger.info("Hello World")
logger.error("Hello World")





