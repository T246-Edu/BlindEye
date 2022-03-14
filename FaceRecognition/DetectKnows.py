import os
import cv2
from FaceRecognition.Faces import Faces


def DetecKnows():
    List_Knows = []
    for faceName in Faces:
        try:
            img = cv2.imread(
                "{}\\FaceRecognition\\Faces\\{}.jpg".format(os.getcwd(), faceName))
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faceCascade = cv2.CascadeClassifier(
                cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=3,
                minSize=(30, 30)
            )

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                roi_color = img[y:y + h, x:x + w]
                try:
                    os.mkdir(
                        "{}\\FaceRecognition\\DetectedFaces".format(os.getcwd()))
                except:
                    pass
                cv2.imwrite('{}\\FaceRecognition\\DetectedFaces\\{}.jpg'.format(
                    os.getcwd(), faceName), roi_color)
                List_Knows.append(faceName)
        except:
            print("Couldn't detect the face, {}".format(faceName))
    return List_Knows
