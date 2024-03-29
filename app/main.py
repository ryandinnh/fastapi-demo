#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
# from models import Item
import json
import requests

import os
import MySQLdb
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html = True), name="static")

DBHOST = os.environ.get('DBHOST')
DBUSER = os.environ.get('DBUSER')
DBPASS = os.environ.get('DBPASS')
DB = "rqd3qmk"

# The URL for this API has a /docs endpoint that lets you see and test
# your various endpoints/methods.

@app.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Hello API", "album_endpoint":"/albums","static_endpoint":"/static"}

#new endpoints for lab 6 
@app.get("/greeting")
def get_greeting():
    return {"Message": "Hello World"}

@app.get("/farewell")
def get_greeting():
    return {"Message": "Bye World"}

@app.get("/albums")
def get_all_albums():
    db = MySQLdb.connect(host=DBHOST, user=DBUSER, passwd=DBPASS, db=DB)
    c = db.cursor(MySQLdb.cursors.DictCursor)
    c.execute("SELECT * FROM albums ORDER BY name")
    results = c.fetchall()
    db.close()
    return results

@app.get("/albums/{id}")
def get_one_album(id):
    db = MySQLdb.connect(host=DBHOST, user=DBUSER, passwd=DBPASS, db=DB)
    c = db.cursor(MySQLdb.cursors.DictCursor)
    c.execute("SELECT * FROM albums WHERE id=" + id)
    results = c.fetchall()
    db.close()
    return results
    
# Start using the "Item" BaseModel
# Post / Delete / Patch methods
# @app.post("/items/{item_id}")
# def add_item(item_id: int, item: Item):
#     return {"item_id": item_id, "item_name": item.name}

# @app.delete("/items/{item_id}")
# def delete_item(item_id: int, item: Item):
#     return {"action": "deleted", "item_id": item_id}

# @app.patch("/items/{item_id}")
# def patch_item(item_id: int, item: Item):
#     return {"action": "patch", "item_id": item_id}
