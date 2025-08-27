from datetime import datetime
from fastapi import FastAPI
from consumer import Consumer
from mongo_dal import MongoDal

app = FastAPI()

mongo_client = MongoDal(host='mongo_db', port=27017)

@app.get('/interesting')
def get_not_interesting():

    try:
        consumer = Consumer(['kafka:29092'])
        interesting_messages = consumer.consume('interesting')

        clean_messages = []
        for message in interesting_messages:
            message = {'time' : datetime.now(),'value' : message.value}
            clean_messages.append(message)
        print(clean_messages)
        mongo_client.insert_many(db_name='messages',
                                 collection_name='interesting-messages',
                                 vals_list=clean_messages)

        consumer.close()

        return 'interesting messages uploaded to mongo'

    except Exception as e:
        print(e)



@app.get('/not-interesting')
def get_not_interesting():

    try:
        consumer = Consumer(['kafka:29092'])
        not_interesting_messages = consumer.consume('not_interesting')

        clean_messages = []
        for message in not_interesting_messages:
            message = {'time': datetime.now(), 'value': message.value}
            clean_messages.append(message)

        mongo_client.insert_many(db_name='messages',
                                 collection_name='not-interesting-messages',
                                 vals_list=clean_messages)

        consumer.close()

        return 'not-interesting messages uploaded to mongo'

    except Exception as e:
        print(e)