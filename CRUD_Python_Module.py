# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'Password' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 
            
    # Creates a method to implement the C in CRUD. 
    def create(self, data):
        try:
            if data is not None: 
                self.collection.insert_one(data)  # data should be dictionary 
                return True
            else: 
                return False
        except Exception as e:
            print(f"Create error: {e}")
            return False

    # Creates a method to implement the R in CRUD.
    def read(self, query):
        try:
            if query is not None:
                # Uses find() to retrieve documents matching query
                results = list(self.collection.find(query))
                return results
            else:
                return []
        except Exception as e:
            print(f"Read error: {e}")
            return []
        
    # Creates a method for the U in CRUD
    def update(self, query, update_data):
        try:
            if query is not None and update_data is not None:
                # Uses update_many() to update matching documents
                results = self.collection.update_many(query, update_data)
                return results.modified_count
            else:
                return 0
        except Exception as e:
            print(f"Update error: {e}")
            return 0
            
    # Creates a method to implement the D in CRUD
    def delete(self, query):
        try:
            if query is not None:
                # Uses delete_many() to remove matching documents
                results = self.collection.delete_many(query)
                return results.deleted_count
            else:
                return 0
        except Exception as e:
            print(f"Delete error: {e}")
            return 0
                