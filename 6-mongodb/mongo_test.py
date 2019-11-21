from pymongo import MongoClient


try:
    client = MongoClient('mongodb://localhost:27017/',
                                 serverSelectionTimeoutMS=1000)
    client.server_info()
    
    print('\n Database Connected\n\n Attempting to insert test data into db')
    
    db = client.test_database
    collection = db.test_collection
    test = {"author": "Raghav"}
    id = collection.insert_one(test).inserted_id
    if not id:
        print ('\n Database insertion failed :(\n')
    else:
        print('\n Databse insertion Successful\n\n MongoDB is Up and Kicking\n')
except Exception as e:
    print ('\n An error occurred: {}\n'.format(e))

    
