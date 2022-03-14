import json
import os
import time
import cv2
import requests
import cloudinary
import cloudinary.uploader


def detectMask(img):
    cloudinary.config(
        cloud_name="dfehchjmf",
        api_key="529222792259839",
        api_secret="TeyRTj4xxcmHaly7ju_oh9TA7_Y",
        secure=True
    )
    url = "https://mask-detection.p.rapidapi.com/mask-detection"
    data = cloudinary.uploader.upload(img)

    if data:
        payload = "{\r\n    \"url\": \"%s\"\r\n}" % (data["url"])
        headers = {
            'content-type': "application/json",
            'x-rapidapi-host': "mask-detection.p.rapidapi.com",
            'x-rapidapi-key': "a74bf07708mshe2753096dd4b303p130c57jsn6e957211b926"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        try:
            print(json.loads(response.text)[0]["mask"]["value"] + " probability: {}".format
                  (json.loads(response.text)[0]["mask"]["probability"]))
        except IndexError:
            print("Error in image")
    else:
        print("problem uploading file")


def MaskDetector():
    vid = cv2.VideoCapture(0)

    while True:
        ret, frame = vid.read()
        print('reading image')
        time.sleep(1)
        cv2.imwrite('{}\\MaskDetector\\image.jpg'.format(os.getcwd()), frame)
        detectMask('{}\\MaskDetector\\image.jpg'.format(os.getcwd()))

        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()
