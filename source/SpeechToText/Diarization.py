#FunASR


"""
from dotenv import load_dotenv
from pyannote.audio import Pipeline

import os

load_dotenv(dotenv_path="../../.env")
HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise RuntimeError("HUGGINGFACE_TOKEN missing")

pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization@2.1",
    revision="main",
    token=HF_TOKEN,
)
# optional: if you KNOW it's two speakers, force 2
diarization = pipeline("speech.wav", num_speakers=2)

for turn, _, speaker in diarization.itertracks(yield_label=True):
    print(f"{turn.start:7.2f} - {turn.end:7.2f}  {speaker}")
"""