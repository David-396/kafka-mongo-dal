from fastapi import FastAPI
from starlette.responses import JSONResponse
from mongo_connect import MongoConnect


app = FastAPI()

mongo_client = MongoConnect(host='mongo_db', port=27017)

@app.get('/get-interesting')
def get_interesting_msgs():
    try:
        messages = mongo_client.get_docs(db_name='messages', collection_name='interesting-messages')

        return JSONResponse(content=messages, status_code=200)

    except Exception as e:
        return JSONResponse(content=e, status_code=400)


@app.get('/get-not-interesting')
def get_interesting_msgs():
    try:
        messages = mongo_client.get_docs(db_name='messages', collection_name='not-interesting-messages')

        return JSONResponse(content=messages, status_code=200)

    except Exception as e:
        return JSONResponse(content=e, status_code=400)
