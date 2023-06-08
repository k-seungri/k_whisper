import whisper
import os
import time

model = whisper.load_model("medium")
# # audio = whisper.load_audio("test_wav.wav")
# result = model.transcribe("test_wav.wav",language='korean')
# print(result["text"])

files = os.listdir('./data/NO')
for file in files:
    s = time.time()
    f = './data/NO/' + file
    result = model.transcribe(f, language='korean')
    e = time.time()
    print(result['text'], e-s)