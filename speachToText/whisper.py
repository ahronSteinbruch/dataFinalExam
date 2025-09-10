from faster_whisper import WhisperModel
import io

class STT:

    model = WhisperModel("tiny", device="cpu", compute_type="int8")

    @staticmethod
    def transcriber(file: bytes) -> str:
        file = io.BytesIO(file)
        segments, info = STT.model.transcribe(file)

        text = ".".join([s.text for s in segments])
        return text

