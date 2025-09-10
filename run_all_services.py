from time import sleep

from Hazard_level_classifier.main_classifier import MainClassifier
from produceData.loadDataprocess import LoadDataprocess
from storeData.dataLoad import DataLoad
from speachToText.controller import TTS_controller
from config import Config

if __name__ == "__main__":
    loadDataprocess = LoadDataprocess(Config.AUDIO_FOLDER)
    sleep(5)
    dataLoad = DataLoad()
    sleep(5)
    tts_controller = TTS_controller()
    sleep(5)
    mainClassifier = MainClassifier()

