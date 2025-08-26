from datetime import datetime

from fastapi import FastAPI
from consumer import Consumer
from consumer.mongo_dal import MongoDal

app = FastAPI()
consumer = Consumer(['localhost:9092'])
mongo_dal = MongoDal(host='localhost', port=9092)

@app.get('/interesting')
def get_not_interesting():
    interesting_messages = consumer.consume('interesting')

    clean_messages = []
    for message in interesting_messages:
        message = {'time' : datetime.now(),'value' : message.value}
        clean_messages.append(message)


@app.get('/not-interesting')
def get_not_interesting():
    not_interesting_messages = consumer.consume('not_interesting')

    clean_messages = []
    for message in not_interesting_messages:
        message = {'time': datetime.now(), 'value': message.value}
        clean_messages.append(message)


