from urllib.request import urlopen
from aiogram.utils.json import json


def to_db():  # this method was used to get json data
    url = ""
    json_url = urlopen(url)
    data = json.loads(json_url.read())
    res = list()
    for d in data:
        if d['category'] == 'Flags' and len(d['emoji']) <= 2:
            res.append(d['emoji'])
    return res


