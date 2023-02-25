"""Method to get channel_id"""
from loader import db
collection = db.videos


def get_channel_id():
    random_doc = collection.aggregate([{"$sample": {"size": 1}}]).next()
    return random_doc['yt_id']
