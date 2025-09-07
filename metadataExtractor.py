from pathlib import Path
import wave
import hashlib


path = Path('/Users/user/Desktop/podcasts/')
class MetadataExtractor:
    @staticmethod
    def extract_metadata(file_path: Path) -> dict:
        file_size = file_path.stat().st_size
        with wave.open(str(file_path), 'rb') as wav_file:
            return {
                "hash": MetadataExtractor.get_file_hash(file_path),
                "filename": file_path.name,
                "path": str(file_path.resolve()),
                "file_size": file_size,
                "channels": wav_file.getnchannels(),
                "sample_width": wav_file.getsampwidth(),
                "framerate": wav_file.getframerate(),
                "nframes": wav_file.getnframes(),
                "duration": wav_file.getnframes() / wav_file.getframerate()
            }

    @staticmethod
    def get_file_hash(file_path, algorithm='sha256'):
        """Calculates the hash of a file's content."""
        hasher = hashlib.new(algorithm)
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(4096)  # Read in 4KB chunks
                if not chunk:
                    break
                hasher.update(chunk)
        return hasher.hexdigest()




