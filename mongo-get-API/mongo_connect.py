from pymongo import MongoClient


class MongoConnect:
    def __init__(self, host, port):
        self.client = MongoClient(host=host, port=port)

    def get_docs(self, db_name, collection_name):
        try:
            db = self.client[db_name]
            collections = db[collection_name]
            messages = collections.find().to_list()

            return messages

        except Exception as e:
            print(e)