import json
from kafka import KafkaProducer

class Publisher:
    def __init__(self, bootstrap_servers):
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                      value_serializer=lambda x: json.dumps(list(x)).encode('utf-8'),
                                      )

        self.interesting_path = r'data/interesting_category_dict.json'
        self.not_interesting_path = r'data/newsgroups_not_interesting.json'

        self.interesting_msgs = self.get_interesting_dict_from_file()
        self.not_interesting_msgs = self.get_not_interesting_dict_from_file()

        self.categories_indexes = self.set_categories_indexes()


    def set_categories_indexes(self):
        categories_indexes = {}
        for k, v in self.interesting_msgs.items():
            categories_indexes[k] = 0

        for k, v in self.not_interesting_msgs.items():
            categories_indexes[k] = 0

        return categories_indexes


    def get_interesting_dict_from_file(self):
        with open(self.interesting_path, 'r', encoding='utf-8')as f:
            newsgroups_interesting = json.load(f)
            return newsgroups_interesting

    def get_not_interesting_dict_from_file(self):
        with open(self.not_interesting_path, 'r', encoding='utf-8') as f:
            newsgroups_not_interesting = json.load(f)
            return newsgroups_not_interesting


    def current_pub_messages(self, interesting : bool):
        msgs_to_pub = []
        current_msgs_dict = self.interesting_msgs if interesting else self.not_interesting_msgs
        categories_added = 0

        for k, v in current_msgs_dict.items():

            if self.categories_indexes[k] == len(v):
                self.categories_indexes[k] = 0

            message = v[self.categories_indexes[k]]
            msgs_to_pub.append(message)
            self.categories_indexes[k] += 1

            categories_added += 1
            if categories_added == 10:
                break

        return msgs_to_pub



    def pub(self):

        interesting_messages = self.current_pub_messages(interesting=True)
        self.producer.send(topic='interesting', value=interesting_messages)

        not_interesting_messages = self.current_pub_messages(interesting=False)
        self.producer.send(topic='not_interesting', value=not_interesting_messages)

        self.producer.flush()
