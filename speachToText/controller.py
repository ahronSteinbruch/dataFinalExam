from pprint import pprint

from config import Config
from utils.mongo_servise.crud import MongoCRUD
from utils.logger import Logger
import logging
from .whisper import STT
from utils.Elastic_service.DAL import DAL

try:
    logger = Logger.get_logger()
except Exception as e:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

URI = Config.MONGO_URI
DB = Config.MONGO_DB
COLLECTION = Config.MONGO_COLLECTION
INDEX = Config.MONGO_COLLECTION


class TTS_controller:
    def __init__(self):
        self.mongo = MongoCRUD(URI, DB, COLLECTION)
        self.es = DAL(INDEX,create_index=False)
        self.whisper = STT()
    def get_all_hash_keys(self) :
        try:
            all_docs = self.es.get_all_empty_text()
            all_hashs = [doc.get("_source").get("hash") for doc in all_docs]
            all_ids = [doc.get("_id") for doc in all_docs]
            return all_hashs,all_ids
        except Exception as e:
            logger.error(f"Failed to fetch documents: {str(e)}")


    def SpeechToText(self, audio: bytes) -> str | None:
        try:
            text =self.whisper.transcriber(audio)
            return text
        except Exception as e:
            logger.error(f"Failed to transcribe audio: {str(e)}")
    def pipeline(self):
        try:
            logger.info("Pipeline started.")
            all_keys = self.get_all_hash_keys()[0]
            all_ids = self.get_all_hash_keys()[1]

            for key,id in zip(all_keys,all_ids):
                file = self.mongo.get_document_by_hash(key)
                text = self.SpeechToText(file.read())

                self.es.update_data(id, {"text": text})

        except Exception as e:
            logger.error(f"Failed to fetch documents: {str(e)}")

if __name__ == "__main__":
    tts_controller = TTS_controller()
    tts_controller.pipeline()