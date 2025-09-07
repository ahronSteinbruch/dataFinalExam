from pathlib import Path
import wave


path = Path('/Users/user/Desktop/podcasts/')
class MetadataExtractor:
    @staticmethod
    def extract_metadata(file_path: Path) -> dict:
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





