from __future__ import print_function
from bs4 import BeautifulSoup
import re
import os
from PIL import Image
import cv2
import requests
import time

NUM_CLUSTERS = 5


def getColorName(colorRGB):
    r, g, b = colorRGB
    data = requests.get(
        "https://www.thecolorapi.com/id?format=html&rgb=({},{},{})".format(int(r), int(g), int(b)))
    soup = BeautifulSoup(data.content, 'html5lib')
    data = soup.find("div", attrs={"class": "text-center"}
                     ).find("a", attrs={"class": "in-api-link"}).text

    data = re.findall('"([^"]*)"', '{}'.format(data))
    print("Name: " + str(data[0]))


def most_common_used_color(img):
    width, height = img.size
    r_total = 0
    g_total = 0
    b_total = 0
    count = 0
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x, y))

            r_total += r
            g_total += g
            b_total += b
            count += 1

    return (r_total/count, g_total/count, b_total/count)


def detectColors():
    vid = cv2.VideoCapture(0)
    while True:
        ret, frame = vid.read()
        print('reading image')
        time.sleep(2)
        cv2.imwrite('{}\\ColorsDetection\\image.jpg'.format(
            os.getcwd()), frame)
        im = Image.open('{}\\ColorsDetection\\image.jpg'.format(os.getcwd()))
        im = im.convert('RGB')
        common_color = most_common_used_color(im)
        r, g, b = common_color
        print("common color (R,G,B): {},{},{}".format(int(r), int(g), int(b)))
        getColorName(common_color)

        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()
