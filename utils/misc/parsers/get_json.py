from urllib.request import urlopen
from aiogram.utils.json import json


def to_db():  # this method was used to get json data
    url = "url_with_json"
    json_url = urlopen(url)
    data = json.loads(json_url.read())
    s = list()
    for lst in data.values():
        for d in lst:
            s.append(d['emoji'])
    emojis = [i for i in s if len(i) == 1]
    return emojis
