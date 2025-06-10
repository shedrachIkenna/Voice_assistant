import vosk
import pyaudio
import json
import os

model_path = r"model\vosk-model-small-en-us-0.15"


if not os.path.exists(model_path):
    print(f"Vosk model not found at {model_path}. Please download it!")
    exit()

model = vosk.Model(model_path)
rec = vosk.KaldiRecognizer(model, 16000)  

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

print("Listening...")
try:
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result["text"]
            if text:
                print(f"You said: {text}")
        else:
            partial = json.loads(rec.PartialResult())
            if partial["partial"]:
                print(f"Partial: {partial['partial']}")
except KeyboardInterrupt:
    print("Stopping...")

finally:
    stream.stop_stream()
    stream.close()
    p.terminate()