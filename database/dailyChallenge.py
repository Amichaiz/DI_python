from pymongo import MongoClient
from random import randint
import requests

client = MongoClient('mongodb://localhost:27017')

db = client['api']
col = db['countries']
print(col)
#
# r = requests.get('https://restcountries.com/v3.1/all')
# data = r.json()
#
# arr = []
# for x in range(10):
#     arr.append({"country": data[randint(1, 100)]['name']['common']})
#
# print(arr)
# #
# x = col.insert_many(arr)

# x = col.insert_one({"test": "hello"})
#

# for x in col.find({},{"_id": 0, "country": 1}).sort("country"):
#     print(x)

for x in col.aggregate([{"$sortByCount": '$country'}]):
    print(x)
