from pathlib import Path
from os import getenv

class Config:
    KAFKA_BROKER = getenv("KAFKA_BROKER", "localhost:9092")
    KAFKA_TOPIC = getenv("KAFKA_TOPIC", "metadata")
    AUDIO_FOLDER = getenv("AUDIO_FOLDER", Path("/podcasts/"))
    MONGO_URI = getenv("MONGO_URI", "mongodb://localhost:27017")
    MONGO_DB = getenv("MONGO_DB", "audio_files")
    MONGO_COLLECTION = getenv("MONGO_COLLECTION", "audio_files")
    MONGO_FS_COLLECTION = getenv("MONGO_FS_COLLECTION", "fs.chunks")
    ELASTIC_HOST = getenv("ELASTIC_HOST", "http://localhost:9200")
    ELASTIC_INDEX = getenv("ELASTIC_INDEX", "audio_files")
    ELASTIC_LOG_INDEX = getenv("ELASTIC_LOG_INDEX", "logy")
    ELASTIC_PORT = getenv("ELASTIC_PORT", 9200)
    ELASTIC_SCHEME = getenv("ELASTIC_SCHEME", "http")
    LOG_LEVEL = "DEBUG"
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    LOG_INDEX = getenv("LOG_INDEX", "log")
    LOG_HOST = getenv("LOG_HOST", "localhost")
    LOG_PORT = getenv("LOG_PORT", 9200)
    FORMAT = "utf-8"
    QUERY = {"query": {
        "bool": {
            "should": [
                {"match":
                    {
                        "text":
                            {
                                "query":
                                    "Genocide Apartheid Massacre Nakba Displacement  Blockade Occupation Refugees ICC BDS",

                                "minimum_should_match": 1,
                                "boost": 2
                            }
                    }

                },
                {"match_phrase": {"text": {"query": "War Crimes", "boost": 2}}},
                {"match_phrase": {"text": {"query": "Humanitarian Crisis", "boost": 2}}},
                {
                    "match":
                        {
                            "text":
                                {

                                    "query":
                                        "Resistance Liberation Gaza Ceasefire Protest UNRWA",

                                    "minimum_should_match": 1
                                }
                        }

                },
                {"match_phrase": {"text": "Free Palestine"}},
                {"match_phrase": {"text": "Freedom Flotilla"}}
            ],
            "minimum_should_match": 1
        }
    }
}