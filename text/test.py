import datetime

from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.adddvb
collection = db.adddvb
post = [
    {
        '_id': 100,
        "a": 1,
        "b": "222aacc",
        'c': [1, 2, 3, 4, 5],
        'date': datetime.datetime.utcnow()
    },
    {
        'title': 'pidici',
        'content': 'gaoxiaoba',
        'tip': 21
    }
]
print(collection.insert_many(post).inserted_ids)

