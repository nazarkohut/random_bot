"""
Contains MongoDB connection and methods.
"""
import pymongo

import config

username = config.DATABASE_USERNAME
password = config.DATABASE_PASSWORD


class DataBase:
    """
    Class for managing MongoDB data and connection.
    """
    def __init__(self):
        self._client = pymongo.MongoClient(
            f"mongodb+srv://{username}:{password}@cluster.f7omn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self._database = self._client.get_database("database")
        self.emojis = self._database.get_collection("emojis")
        self.flags = self._database.get_collection("flags")
        self.videos = self._database.get_collection("youtube_videos")

    def add_emojis(self, lst):
        self.emojis.insert({"emojis_list": lst})

    def get_emojis_list(self):
        d = self.emojis.find({}, {"emojis_list": 1, "_id": 0})
        d = next(d)
        return d["emojis_list"]

    def add_flags(self, lst):
        self.flags.insert({"flags": lst})

    def get_flags_list(self):
        d = self.flags.find({}, {"flags": 1, "_id": 0})
        d = next(d)
        return d["flags"]


