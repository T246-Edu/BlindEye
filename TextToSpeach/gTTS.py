import pyttsx3


def sayWords(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
