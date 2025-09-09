# from pymongo import MongoClient
# from bson import ObjectId
# from gridfs import GridFS
# from faster_whisper import WhisperModel
# from io import BytesIO
# from pydub import AudioSegment
# import tempfile
# import os
# from pathlib import Path
# import shutil
# from config import Config
#
# class STT:
#     def _init_(self,model_name="tiny", model_folder="models"):
#         self.model_path = Path(model_folder) / f"faster-whisper-{model_name}"
#         self.model_path.mkdir(parents=True, exist_ok=True)
#
#         if any(self.model_path.iterdir()):
#             self.model = WhisperModel(str(self.model_path), device="cpu", compute_type="int8")
#         else:
#             self.model = WhisperModel(model_name, device="cpu", compute_type="int8")
#             cache_dir = Path.home() / ".cache" / "huggingface" / "hub"
#             for p in cache_dir.glob(f"models--Systran--faster-whisper-{model_name}*"):
#                 if p.is_dir():
#                     shutil.copytree(p, self.model_path, dirs_exist_ok=True)
#                     break
#
#
#     def transcribe_from_gridfs(self, audio_bytes) -> str:
#
#         audio_segment = AudioSegment.from_file(BytesIO(audio_bytes), format="wav")
#         wav_io = BytesIO()
#         audio_segment.export(wav_io, format="wav")
#         wav_io.seek(0)
#
#
#         with tempfile.NamedTemporaryFile(suffix=".wav", delete=True) as tmp:
#             tmp.write(wav_io.read())
#             tmp.flush()
#
#             segments, _ = self.model.transcribe(tmp.name, beam_size=5, language="en")
#         return " ".join([seg.text for seg in segments])

