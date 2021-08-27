import pymongo

import config

username = config.DATABASE_USERNAME
password = config.DATABASE_PASSWORD


class DataBase:
    def __init__(self):
        self._client = pymongo.MongoClient(
            f'mongodb+srv://{username}:{password}@cluster.f7omn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
        self._database = self._client.get_database("database")
        self.emojis = self._database.get_collection("emojis")

    def add_emojis(self, lst):
        self.emojis.insert({'emojis_list': lst})

    def get_emojis_list(self):
        d = self.emojis.find({}, {'emojis_list': 1, '_id': 0})
        d = next(d)
        return d['emojis_list']
