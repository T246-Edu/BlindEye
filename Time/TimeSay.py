import time


def DateTime():
    timeNow = "{}".format(time.asctime(time.localtime(time.time())))
    return timeNow
