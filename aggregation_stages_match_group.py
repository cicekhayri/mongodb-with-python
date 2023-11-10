import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MONGODB_URI)

db = client.bank

accounts_collection = db.accounts

select_by_balance = {"$match": {"balance": {"$lt": 1000}}}

separate_by_account_calculate_avg_balance = {
    "$group": {"_id": "$account_type", "avg_balance": {"$avg": "$balance"}}
}

pipeline = [
    select_by_balance,
    separate_by_account_calculate_avg_balance,
]

results = accounts_collection.aggregate(pipeline)

print()
print(
    "Average balance of checking and savings accounts with balance of less than $1000:\n"
)

for item in results:
    pprint.pprint(item)

client.close()
