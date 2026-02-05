from faster_whisper import WhisperModel

def transcribe_speech():
    model = WhisperModel("base", device="cpu", compute_type="int8")

    segments, info = model.transcribe("data/speech.wav")

    return (segments, info)


#seg = transcribe_speech()

#for s in seg[0]:
#    print(s.text)

