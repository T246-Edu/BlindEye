import psutil
from TextToSpeach import sayWords


def battery():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    if plugged == False:
        plugged = "Not Plugged In"
    else:
        plugged = "Plugged In"
    result = "{} ,{}%".format(plugged, percent)
    print(result)
    # sayWords(result)
