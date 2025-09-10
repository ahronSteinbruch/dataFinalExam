import base64
from config import Config

format = Config.FORMAT

class Decoder:

    @staticmethod
    def decode_base64(data):
        return base64.b64decode(data).decode(format)





