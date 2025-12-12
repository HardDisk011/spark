import pyttsx3

def say(engine, answer):
    engine.say(answer)
    engine.runAndWait()