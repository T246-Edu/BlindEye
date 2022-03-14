import json
import cloudinary
import cv2
import requests
import os
import cloudinary.uploader


def upload(imageURL):
    cloudinary.config(
        cloud_name="dfehchjmf",
        api_key="529222792259839",
        api_secret="TeyRTj4xxcmHaly7ju_oh9TA7_Y",
        secure=True
    )
    data = cloudinary.uploader.upload(imageURL)["url"]
    return data


def recognizer(IMGUrl):
    urll = upload(IMGUrl)

    url = "https://emotion-detection2.p.rapidapi.com/emotion-detection"

    payload = "{\r\"url\": \"%s\"\r}" % (urll)
    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "emotion-detection2.p.rapidapi.com",
        'x-rapidapi-key': "a74bf07708mshe2753096dd4b303p130c57jsn6e957211b926"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    try:
        print("The person is: " +
              str(json.loads(response.text)[0]["emotion"]["value"]))
    except KeyError:
        pass


def detection():
    vid = cv2.VideoCapture(0)
    while True:
        ret, frame = vid.read()
        cv2.imwrite("{}\\emotionDetection\\face.jpg".format(
            os.getcwd()), frame)
        recognizer("{}\\emotionDetection\\face.jpg".format(os.getcwd()))

        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()
