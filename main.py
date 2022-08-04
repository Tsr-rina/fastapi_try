from fastapi import FastAPI
from enum import Enum
from typing import Union
import json

new_ver = "2"


json_open = open('art_info.json', 'r')
json_load = json.load(json_open)

app = FastAPI()

# country_select_ver
@app.get("/items/art/{version}/{country}")
async def read_art_c(version:str, country:str):

    if country in json_load:
        global judge
        judge = True
    if version[-1] == new_ver and judge==True:
        return json_load[country]
    else:
        if version[-1] != new_ver:
            return "{} is no support".format(version)
        else:
            return "No Page"

# general_select_ver
@app.get("/items/art/{version}")
async def read_art_v(version:str):
    if version[-1] == new_ver:
        return json_load
    else:
        return "現在のバージョンはv{}です".format(new_ver)