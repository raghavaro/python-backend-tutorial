from pymongo import MongoClient
client = MongoClient()
#client = MongoClient('mongodb://localhost:27017/')

db = client.test_database
print('\nDatabase: {}'.format(db))
collection = db.test_collection
print('\nCollection: {}'.format(collection))

if db and collection:
    print('\n Mongo Connection Successful\n')

