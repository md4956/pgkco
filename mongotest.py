from flask import Flask
from pymongo import MongoClient
import datetime
import pprint

client = MongoClient()
db = client.pgco345

post = {"author": "aaa ",
        "text": "My first blog postpostpostpostpost!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts3 = db.postssss

post_id = posts3.insert_one(post).inserted_id
print(post_id)

pprint.pprint(posts3.find_one({"author": "asghar"}))
client = MongoClient('localhost', 27017)
