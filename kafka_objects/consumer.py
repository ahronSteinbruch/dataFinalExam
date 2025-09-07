from kafka import KafkaConsumer
import json


class Consumer:
    def __init__(self, topics:list[str]):
        """
        Initializes the Kafka Consumer.

        Args:
            topic (str): The Kafka topic to subscribe to.
        """
        self.topics = topics
        self.consumer = KafkaConsumer(
            *self.topics,
            group_id='mongo-writer-group',
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest'  # Start reading from the beginning of the topic
        )
        print(f"Kafka consumer subscribed to topic '{self.topics}'.")

    def get_consumer(self):
        return self.consumer

