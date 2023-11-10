import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient

from bson.objectid import ObjectId


load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MONGODB_URI)

db = client.bank

accounts_collection = db.accounts

document_to_find = {"_id": ObjectId("654dea47d91d97979fd1ad36")}

result = accounts_collection.find_one(document_to_find)
pprint.pprint(result)

client.close()
