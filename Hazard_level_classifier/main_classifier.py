from .decoder import Decoder
from utils.Elastic_service.DAL import DAL
from config import Config
from utils.logger import Logger
import logging
from pprint import pprint
INDEX = Config.ELASTIC_INDEX

#I used this query I know it's not the best but but I have no time to make it better
hard_code_query = Config.QUERY
try:
    logger = Logger.get_logger()
except Exception as e:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

class MainClassifier:
    """ rate the severity of the text and insert the results to elasticsearch """


    def __init__(self):
        self.score_dict = {}
        self.THRESHOLD = 0.5
        Severe_Hostile_words =Decoder.decode_base64(
            "R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT")
        hostile_words =Decoder.decode_base64(
            "RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ==")
        self.hostile_words = hostile_words.split(",")
        self.severe_Hostile_words = Severe_Hostile_words.split(",")
        self.es = DAL(INDEX,create_index=False)


    def get_score_occurrences(self, max_score,score):
        """ get the score occurrences """
        bds_percent = score / max_score
        bds_threat_level = "high"
        if bds_percent < 0.3:
            bds_threat_level = "low"
        elif bds_percent < 0.7:
            bds_threat_level = "medium"
        is_bds = bds_percent > 0.5

        return bds_percent,bds_threat_level,is_bds





    def init_score_dict(self):
        """ init the score dict with all the ids """
        try:
            all_docs = self.es.get_all_empty_text()
            all_ids = [doc.get("_id") for doc in all_docs]
            for id in all_ids:
                self.score_dict[id] = 0
            logger.info("Score dict initialized successfully.")
        except Exception as e:
            logger.error(f"Failed to initialize score dict: {e}")


    def rate(self):
        """ rate the severity of the text for all the documents """
        try:
            threatening_docs = self.es.crud.search_data(hard_code_query)
            docs = threatening_docs.get("hits").get("hits")
            pprint(docs)
            max_score = threatening_docs["hits"]["max_score"]
            logger.info(f"Max score: {max_score}")
            print(max_score)
            for doc in docs:
                id = doc.get("_id")
                score = doc.get("_score")
                self.score_dict[id] = score
            return max_score


        except Exception as e:
            logger.error(f"Failed to rate: {e}")


    def update(self,max_score):
        """ update the elasticsearch with the results """
        try:
            for id in self.score_dict:
                result = self.get_score_occurrences(max_score,self.score_dict[id])
                field_updates = {
                    "bds_percent":result[0],
                    "bds_threat_level":result[1],
                    "is_bds":result[2]
                }
                self.es.update_data(id,{"doc":field_updates})
                logger.info(f"Updated {id} successfully.")
        except Exception as e:
            logger.error(f"Failed to update: {e}")

    def pipeline(self):
        """ run the pipeline """
        try:
            self.init_score_dict()
            max_score = self.rate()
            self.update(max_score)
            logger.info("Pipeline completed successfully.")
        except Exception as e:
            logger.error(f"Failed to run pipeline: {e}")

if __name__ == "__main__":
   m = MainClassifier()
   m.pipeline()



