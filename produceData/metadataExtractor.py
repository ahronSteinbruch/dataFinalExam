from pathlib import Path
import wave
from logger import Logger
import logging

try:
    logger = Logger.get_logger()
except Exception as e:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)


path = Path('/Users/user/Desktop/podcasts/')
class MetadataExtractor:
    @staticmethod
    def extract_metadata(file_path: Path) -> dict:
        logger.info(f"Extracting metadata for {file_path.name}")
        file_size = file_path.stat().st_size
        with wave.open(str(file_path), 'rb') as wav_file:
            return {
                "filename": file_path.name,
                "path": str(file_path.resolve()),
                "file_size": file_size,
                "channels": wav_file.getnchannels(),
                "sample_width": wav_file.getsampwidth(),
                "framerate": wav_file.getframerate(),
                "nframes": wav_file.getnframes(),
                "duration": wav_file.getnframes() / wav_file.getframerate()
            }






