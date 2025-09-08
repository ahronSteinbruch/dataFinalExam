from kafka import KafkaProducer
import json
from logger import Logger
import logging

try:
    logger = Logger.get_logger()
except Exception as e:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

class Producer:
    """Kafka Producer"""
    def __init__(self,bootstrap_servers = 'localhost:9092',
                 encode = 'utf-8'):
        self.producer = KafkaProducer(bootstrap_servers=[bootstrap_servers],
                             value_serializer=lambda x:
                             json.dumps(x, default=str).encode(encode))
        logger.info("Kafka producer initialized.")

    def publish_message(self,topic,message):
        """Publish a message to a Kafka topic."""
        self.producer.send(topic, message)
        self.producer.flush()