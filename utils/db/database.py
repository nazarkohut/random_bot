import pymongo

import config

username = config.DATABASE_USERNAME
password = config.DATABASE_PASSWORD


class DataBase:
    def __init__(self):
        self._client = pymongo.MongoClient(
            f'mongodb+srv://{username}:{password}@cluster.f7omn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
        self._database = self._client.get_database("database")
        self.color = self._database.get_collection("color")

    def add_color(self):
        self.color.insert_one({'color': ''})
