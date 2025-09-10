from time import sleep

from Hazard_level_classifier.main_classifier import MainClassifier
from produceData.loadDataprocess import LoadDataprocess
from storeData.dataLoad import DataLoad
from speachToText.controller import TTS_controller
from config import Config

if __name__ == "__main__":
    loadDataprocess = LoadDataprocess(Config.AUDIO_FOLDER)
    sleep(500)
    dataLoad = DataLoad()
    sleep(500)
    #i get error here but it's not important
    try:
        tts_controller = TTS_controller()
    except Exception as e:
        print(e)
    sleep(500)
    mainClassifier = MainClassifier()
    mainClassifier.pipeline()

