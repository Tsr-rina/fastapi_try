from fastapi import FastAPI
from enum import Enum
from typing import Union

class ModelName(str, Enum):
    Hon = "Kim"
    Woo = "Choen"

fake_items_db = [
    {"item_name": "Apple"},
    {"item_name": "Banana"},
    {"item_name": "Lemon"}
]

app = FastAPI()

@app.get("/items/art/{country}")
async def read_art(country:str):
    a = {"Hello_Art":country}
    info = {
        'product':[{
            'p_name':'星の力',
            'p_year':1999,
            'p_genre':'pop',
        }],
        'author':[{
            'a_name':'Tyanri-',
            'a_birthday':'2102-13-19',
            'a_from': 'Japan',
            'a_info': 'アプリ作るの大好き絵を描くの大好きゲーム大好き'
        }]
    }
    return info

@app.get("/items/{item_id}")
async def read_items(item_id:str, q:Union[str, None]=None):
    if q:
        return {"item_id":item_id, "q":q}
    return {"item_id":item_id}

@app.get("/items/")
async def read_item(skip:int=0, limit:int=10):
    return fake_items_db[skip: skip+limit]

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path":file_path}

@app.get("/name/{model_name}")
async def read_user_me(model_name:ModelName):
    if model_name == ModelName.Hon:
        return {"model_name":model_name, "message":"ATEEZ"}

@app.get("/{item_id}")
# @app.オペレーション →デコレータ
# @app.post()
# @app.put()
# @app.delete()
async def read_root(item_id:str):
    # return {"Hello":"World!"}
    return {"Hello":item_id}