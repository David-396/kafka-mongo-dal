from fastapi import FastAPI
from publisher import Publisher

app = FastAPI()


publisher = Publisher(['kafka:9092'])


@app.get('/')
def publish_20_messages():
    try:
        publisher.pub()

        return 'messages published successfully'

    except Exception as e:
        print(e)

