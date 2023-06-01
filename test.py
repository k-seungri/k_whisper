import k_whisper

model = k_whisper.load_model("base")
result = model.transcribe("temp.wav")
print(result["text"])