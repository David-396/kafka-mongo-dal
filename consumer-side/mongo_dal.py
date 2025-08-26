from pymongo import MongoClient

class MongoDal:
    def __init__(self, host, port):

        self.client = MongoClient(
            host=host,
            port=port,
            )

    def insert_one(self, db_name : str, collection_name : str, dict_val : dict):
        db = self.client[db_name]
        collection = db[collection_name]
        collection.insert_one(dict_val)

    def insert_many(self, db_name : str, collection_name : str, vals_list : list):
        db = self.client[db_name]
        collection = db[collection_name]
        collection.insert_many(vals_list)