import pyttsx3 as tts

engine = tts.init()
msg = "How do you do?"
speed = 50

engine.setProperty("rate", speed)
engine.say(msg)
engine.runAndWait()
