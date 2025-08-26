import uvicorn
from fastapi import FastAPI
from producer.publisher import Publisher

app = FastAPI()

interesting_tmp_start_index = 0
not_interesting_tmp_start_index = 0

interesting_tmp_end_index = 10
not_interesting_tmp_end_index = 10


publisher = Publisher()


@app.get('/')
def publish_20_messages():
    global interesting_tmp_end_index, not_interesting_tmp_end_index, interesting_tmp_start_index, not_interesting_tmp_start_index

    publisher.pub(interesting_tmp_start_index, not_interesting_tmp_start_index, interesting_tmp_end_index, not_interesting_tmp_end_index)

    interesting_tmp_start_index += 10
    not_interesting_tmp_start_index += 10

    interesting_tmp_end_index += 10
    not_interesting_tmp_end_index +=10

    return 'messages published successfully'

