from ShutDown import shutdown
#from TextToSpeach import sayWords
from Time import DateTime
from FaceRecognition import detection1
#from BatteryLvl import battery
from ColorsDetection import detectColors
from Location import location
from MaskDetector import MaskDetector
from OCR import TextDetector
from ObjectDetection import DetectObjetsCam
from emotionDetection import detection
import threading as thread
from brandRecommendation import rcommecdation
while True:
    Text = input()
    if Text == "t":
        print(DateTime())
    elif Text == "f":
        colors = thread.Thread(target=detection1)
        colors.start()
    #elif Text == "b":
        #battery()
    elif Text == "s":
        shutdown()
    elif Text == "l":
        llocation = location()
        print(llocation)
    elif Text == "c":
        colors = thread.Thread(target=detectColors)
        colors.start()
    elif Text == "m":
        colors = thread.Thread(target=MaskDetector)
        colors.start()
    elif Text == "w":
        colors = thread.Thread(target=TextDetector)
        colors.start()
    elif Text == "o":
        colors = thread.Thread(target=DetectObjetsCam)
        colors.start()
    elif Text == "d":
        colors = thread.Thread(target=detection)
        colors.start()
    elif Text == "r":
        rcommecdation(input("Enter Text: "))
