# Create a class that would repsresent all basic CRUD operations with MongoDB.

from pymongo import MongoClient

class MongoDB_CRUD:
    def __init__(self, host='localhost', port=27017, db_name='mydatabase', collection_name='mycollection'):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create_document(self, document):
        result = self.collection.insert_one(document)
        return result.inserted_id

    def read_document(self, query):
        result = self.collection.find_one(query)
        return result

    def update_document(self, query, new_values):
        result = self.collection.update_one(query, {'$set': new_values})
        return result.modified_count

    def delete_document(self, query):
        result = self.collection.delete_one(query)
        return result.deleted_count

# Example usage:
# Initialize the MongoDB_CRUD class
mongo_crud = MongoDB_CRUD()

# Create a document
new_document = {'name': 'Alice', 'age': 30}
new_document_id = mongo_crud.create_document(new_document)

# Read a document
query = {'name': 'Alice'}
result = mongo_crud.read_document(query)
print(result)

# Update a document
update_query = {'name': 'Alice'}
new_values = {'age': 31}
modified_count = mongo_crud.update_document(update_query, new_values)
print(f'Modified {modified_count} document')

# Delete a document
delete_query = {'name': 'Alice'}
deleted_count = mongo_crud.delete_document(delete_query)
print(f'Deleted {deleted_count} document')