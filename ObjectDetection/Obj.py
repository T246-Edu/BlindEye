import json
import os
import requests
import ObjectDetection.uploader as upload
import cv2
import time


def ObjectDetector(ImagePath):
    data = {}
    url = "https://ai-image-classifier.p.rapidapi.com/detect"
    querystring = {
        "img_url": "{}".format(upload.upload(ImagePath))}
    headers = {
        'x-rapidapi-host': "ai-image-classifier.p.rapidapi.com",
        'x-rapidapi-key': "a74bf07708mshe2753096dd4b303p130c57jsn6e957211b926"
    }
    response = json.loads(requests.request(
        "GET", url, headers=headers, params=querystring).text)
    for x in list(response["data"]):
        if (x["class"]) in data.keys():
            data[x["class"]] += 1
        else:
            data[x["class"]] = 1
    for key, val in data.items():
        print("There are {} {}s in the image".format(val, key))
    time.sleep(1)


def DetectObjetsCam():
    vid = cv2.VideoCapture(0)
    while(True):
        ret, frame = vid.read()
        cv2.imwrite(os.getcwd() + "\\ObjectDetection\\frame.jpg", frame)
        ObjectDetector(os.getcwd() + "\\ObjectDetection\\frame.jpg")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()
