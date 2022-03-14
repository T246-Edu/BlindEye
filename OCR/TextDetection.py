import json
import os
import time
import cv2
import requests
import cloudinary
import cloudinary.uploader


def ImgToText(imageURL):
    cloudinary.config(
        cloud_name="dfehchjmf",
        api_key="529222792259839",
        api_secret="TeyRTj4xxcmHaly7ju_oh9TA7_Y",
        secure=True
    )
    data = cloudinary.uploader.upload(imageURL)
    url = "https://image-text-recognition.p.rapidapi.com/recognite_by_url"

    payload = "url={}".format(data["url"])
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-host': "image-text-recognition.p.rapidapi.com",
        'x-rapidapi-key': "a74bf07708mshe2753096dd4b303p130c57jsn6e957211b926"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print("Language: " + json.loads(response.text)["language"] + "\n")
    print("Text: " + json.loads(response.text)["text"])


def TextDetector():
    vid = cv2.VideoCapture(0)
    while True:
        ret, frame = vid.read()
        print('reading image')
        time.sleep(1)
        cv2.imwrite('{}\\OCR\\image.jpg'.format(os.getcwd()), frame)
        ImgToText('{}\\OCR\\image.jpg'.format(os.getcwd()))

        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()
