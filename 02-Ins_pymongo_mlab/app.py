from pymongo import MongoClient

client = MongoClient("mongodb://admin:DataRocks!@ds243295.mlab.com:43295/heroku_hs5242f2")

db = client.heroku_hs5242f2

another_collection = db.another_collection

sample_doc = {"author": "Matt",
			"favorite language": "Python",
			"hobbies": ["coding", "music", "rugby"]}

another_collection.insert_one(sample_doc)

import pprint
for post in another_collection.find():
	pprint.pprint(post)