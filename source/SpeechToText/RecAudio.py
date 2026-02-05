import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

class RecordAudio:
    def __init__(self):
        self.recorded = []
        self.fs = 44100
        self.channels = 1
        self.store = 'data/speech.wav'

    def callback(self, indata, frames, time, status):
        if status:
            print(f"[Audio status] {status}")

        self.recorded.append(indata.copy())

    def record_audio(self,):
        self.recorded = []

        print("Recording...")

        with sd.InputStream(samplerate=self.fs, callback=self.callback, channels=self.channels):
            input()

        audio = np.concatenate(self.recorded, axis=0)
        write(self.store, self.fs, audio)
        print("Saved speech.wav")

        return None




"""
import speech_recognition as sr

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")

            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()
            print("You said:", text)

            if "exit" in text:
                print("Exiting program...")
                break

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Could not understand audio")

    except KeyboardInterrupt:
        print("Program terminated by user")
        break
"""