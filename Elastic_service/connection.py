import os
from pprint import pprint
from elasticsearch import Elasticsearch

class ConnES:
    _instance = None

    def __init__(self, host=None, port=None,scheme=None):
        # Load from environment if not provided
        self.host = host or os.getenv("ELASTIC_HOST", "localhost")
        self.port = port or int(os.getenv("ELASTIC_PORT", 9200))
        self.scheme = scheme or os.getenv("ELASTIC_SCHEME", "http")
        self._client = None

    @classmethod
    def get_instance(cls, host=None, port=None):
        """
        Singleton accessor — returns the same instance every time.
        Host/port can be overridden on the first call only.
        """
        if cls._instance is None:
            cls._instance = cls(host, port)
        return cls._instance

    def connect(self):
        if self._client is None:
            try:
                self._client = Elasticsearch(
                    f"{self.scheme}://{self.host}:{self.port}"
                )
                client_info = self._client.info()
                print(f"Connected to Elasticsearch at {self.host}:{self.port}!")
                pprint(client_info.body)
            except Exception as e:
                print(f"Failed to connect to Elasticsearch: {e}")
        return self._client


