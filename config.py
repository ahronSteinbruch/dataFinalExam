from pathlib import Path

class Config:
    KAFKA_BROKER = "localhost:9092"
    KAFKA_TOPIC = "metadata"
    AUDIO_FOLDER = Path("/podcasts/")
    MONGO_URI = "mongodb://localhost:27017"
    MONGO_DB = "audio_files"
    MONGO_COLLECTION = "audio_files"
    MONGO_FS_COLLECTION = "fs.chunks"
    ELASTIC_HOST = "http://localhost:9200"
    ELASTIC_INDEX = "audio_files"
    ELASTIC_LOG_INDEX = "logy"
    ELASTIC_PORT = 9200
    ELASTIC_SCHEME = "http"
    ELASTIC_USERNAME = "elastic"
    ELASTIC_PASSWORD = "elastic"
    ELASTIC_API_KEY = "elastic"
    LOG_LEVEL = "DEBUG"
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    LOG_INDEX = "log"
    LOG_HOST = "localhost"
    LOG_PORT = 9200
