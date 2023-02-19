"""
Contains flags emojis parser method.
"""
from urllib.request import urlopen
from aiogram.utils.json import json


def get_flags() -> list:
    """
    This method was used to get JSON data from one of the internet resources.
    """
    url = ""
    json_url = urlopen(url)
    data = json.loads(json_url.read())
    res = []
    for d in data:
        if d["category"] == "Flags" and len(d["emoji"]) <= 2:
            res.append(d["emoji"])
    return res
