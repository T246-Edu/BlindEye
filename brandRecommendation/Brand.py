import json
import requests


def rcommecdation(text):
    url = "https://brand-recommendation.p.rapidapi.com/brand-recommendation"

    querystring = {"domain": "generic"}

    payload = "[\r\n    {\r\n        \"id\": 1,\r\n        \"language\": \"en\",\r\n        \"text\": \"%s\"\r\n    }\r\n]" % (
        text)
    headers = {
        'content-type': "application/json",
        'accept': "application/json",
        'x-rapidapi-host': "brand-recommendation.p.rapidapi.com",
        'x-rapidapi-key': "a74bf07708mshe2753096dd4b303p130c57jsn6e957211b926"
    }

    response = requests.request(
        "POST", url, data=payload, headers=headers, params=querystring)
    try:
        print(json.loads(response.text)[0]["predictions"][0]["prediction"])
    except:
        pass
