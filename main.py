from fastapi import FastAPI
from enum import Enum
from typing import Union
import json


class ModelName(str, Enum):
    Hon = "Kim"
    Woo = "Choen"

fake_items_db = [
    {"item_name": "Apple"},
    {"item_name": "Banana"},
    {"item_name": "Lemon"}
]


new_ver = "2"


json_open = open('art_info.json', 'r')
json_load = json.load(json_open)

app = FastAPI()

# 国指定ver
@app.get("/items/art/{version}/{country}")
async def read_art_c(version:str, country:str):
    a = {"Hello_Art":country}
    if version[-1] == new_ver:
        return json_load[country]
    else:
        if version[-1] != new_ver:
            return "{} is no support".format(version)
        else:
            return {"X":"Japan"}
@app.get("/items/art/{version}")
async def read_art_v(version:str):
    if version[-1] == new_ver:
        return json_load
    else:
        return "現在のバージョンはv{}です".format(new_ver)

# @app.get("/items/{item_id}")
# async def read_items(item_id:str, q:Union[str, None]=None):
#     if q:
#         return {"item_id":item_id, "q":q}
#     return {"item_id":item_id}

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