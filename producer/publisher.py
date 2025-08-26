import json
from datetime import time

from kafka import KafkaProducer

class Publisher:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                      value_serializer=lambda x: json.dumps(list(x)).encode('utf-8'))

        self.interesting_path = r'.\data\newsgroups_interesting.json'
        self.not_interesting_path = r'.\data\newsgroups_not_interesting.json'

        self.newsgroups_interesting = self.get_interesting_list()
        self.newsgroups_not_interesting = self.get_not_interesting_list()


    def get_interesting_list(self):
        with open(self.interesting_path, 'r', encoding='utf-8')as f:
            newsgroups_interesting = json.load(f)
            return newsgroups_interesting

    def get_not_interesting_list(self):
        with open(self.not_interesting_path, 'r', encoding='utf-8') as f:
            newsgroups_not_interesting = json.load(f)
            return newsgroups_not_interesting


    def pub(self,interesting_start_index, not_interesting_start_index, interesting_end_index, not_interesting_end_index):

        interesting_message = self.newsgroups_interesting[interesting_start_index:interesting_end_index]
        self.producer.send(topic='interesting', value=interesting_message)

        not_interesting_message = self.newsgroups_not_interesting[not_interesting_start_index:not_interesting_end_index]
        self.producer.send(topic='not_interesting', value=not_interesting_message)

        self.producer.flush()