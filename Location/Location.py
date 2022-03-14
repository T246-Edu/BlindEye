from geopy.geocoders import Nominatim
import json
from urllib.request import urlopen


def location():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    IP = data['ip']
    org = data['org']
    city = data['city']
    country = data['country']
    region = data['region']
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode("{}".format(region))
    return (getLoc.address)
