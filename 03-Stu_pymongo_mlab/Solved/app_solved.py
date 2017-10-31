from pymongo import MongoClient

# Create db connection
client = MongoClient('mongodb://admin:DataRocks!@ds243285.mlab.com:43285/heroku_lm19wcqp')


# Create a database
db = client.heroku_lm19wcqp

# Create a collection
new_collection = db.new_collection

user_info = {}

# Prompt for users input
name = input("What is your name? ")
age = int(input("How old are you? "))
movie_amount = int(input("How many favorite movies do you have? "))

movies = []

# Ask for favorite movies
for x in range(movie_amount):
    movie = input("What is a favorite movie of yours? ")
    movies.append(movie)

# Create Dictionary
user_info = {"Name": name,
             "age": age,
             "Favorite Movies": movies}

# Insert user dictionary into DB
db.new_collection.insert_one(user_info)

# Print documents in the collection
import pprint
for post in new_collection.find():
    pprint.pprint(post["Name"] + " has " + str(len(post["Favorite Movies"])))