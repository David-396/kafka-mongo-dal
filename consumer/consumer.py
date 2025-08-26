import json
from kafka import KafkaConsumer


class Consumer:
    def __init__(self, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers


    def consume(self, topic):
        messages = KafkaConsumer(topic,
                                 group_id='group-1',
                                 value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                 bootstrap_servers=self.bootstrap_servers,
                                 consumer_timeout_ms=10000)

        return messages