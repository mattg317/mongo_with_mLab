from pymongo import MongoClient

client = MongoClient('mongodb://admin:DataRocks!@ds243285.mlab.com:43285/heroku_lm19wcqp')

# Create a database
db = client.heroku_lm19wcqp

# Create a collection
new_collection = db.new_collection

# # Create a document
sample_doc = {"author": 'Matt',
               "favorite_language": "Python",
               "hobbies": ["lifting", "coding", "rugby"]}
#
# # Insert document into collection
new_collection.insert_one(sample_doc)
#
import pprint
for post in new_collection.find():
    pprint.pprint(post)