import whisper
print("started!")
model = whisper.load_model("base")
result = model.transcribe("./audio/Lecture.mp3", fp16=False)
f = open("./Translate/Lecture.txt", "w")
f.write(result["text"])
f.close()
print("done!")
