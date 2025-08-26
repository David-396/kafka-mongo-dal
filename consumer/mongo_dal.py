from pymongo import MongoClient

class MongoDal:
    def __init__(self, host, port):

        self.client = MongoClient(
            host=host,
            port=port,
            )

    def insert_one(self, dict_val):
