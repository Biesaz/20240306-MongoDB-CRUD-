# https://github.com/CodeAcademy-Online/python-new-material-level2/wiki/Mongo-DB---lesson-2:-PyMongo-and-CRUD-operations

# from pymongo import MongoClient
# from pymongo.database import Database
# from pymongo.collection import Collection
# from typing import Dict, List

# def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
#     client = MongoClient(host, port)
#     database = client[db_name]
#     return database

# def find_documents(collection: Collection, query: Dict) -> List[Dict]:
#     documents = collection.find(query)
#     return list(documents)

# # Example usage
# if __name__ == "__main__":
#     # Connection details
#     mongodb_host = 'localhost'
#     mongodb_port = 27017
#     database_name = 'mydatabase'
#     collection_name = 'mycollection'

#     # Connect to MongoDB
#     db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

#     # Retrieve a specific collection
#     collection = db[collection_name]

#     # Read (Query) Operation
#     query = {"name": "John Doe"}
#     results = find_documents(collection, query)
#     print("Matching documents:")
#     for result in results:
#         print(result)

# ##################################################
# from pymongo import MongoClient
# from pymongo.database import Database
# from pymongo.collection import Collection
# from typing import Dict, List


# def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
#     client = MongoClient(host, port)
#     database = client[db_name]
#     return database


# def find_documents(collection: Collection, query: Dict) -> List[Dict]:
#     documents = collection.find(query)
#     return list(documents)


# # Example usage
# if __name__ == "__main__":
#     # Connection details
#     mongodb_host = "localhost"
#     mongodb_port = 27017
#     database_name = "persons"
#     collection_name = "employees_night_shift"

#     # Connect to MongoDB
#     db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

#     # Retrieve a specific collection
#     collection = db[collection_name]

#     # Read (Query) Operation
#     query = {"age": 40, "name": "Sharon"}
#     results = find_documents(collection, query)
#     print("Matching documents:")
#     for result in results:
#         print(result)        

##################################################
# from pymongo import MongoClient
# from pymongo.database import Database
# from pymongo.collection import Collection
# from typing import Dict

# def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
#     client = MongoClient(host, port)
#     database = client[db_name]
#     return database

# def update_document(collection: Collection, query: Dict, update: Dict) -> int:
#     result = collection.update_many(query, {"$set": update})
#     return result.modified_count

# # Example usage
# if __name__ == "__main__":
#     # Connection details
#     mongodb_host = 'localhost'
#     mongodb_port = 27017
#     database_name = 'mydatabase'
#     collection_name = 'mycollection'

#     # Connect to MongoDB
#     db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

#     # Retrieve a specific collection
#     collection = db[collection_name]

#     # Update Operation
#     query = {"name": "John Doe"}
#     update = {"age": 35}
#     modified_count = update_document(collection, query, update)
#     print(f"Modified {modified_count} documents")

######################################################
# from pymongo import MongoClient
# from pymongo.database import Database
# from pymongo.collection import Collection
# from typing import Dict

# def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
#     client = MongoClient(host, port)
#     database = client[db_name]
#     return database

# def delete_documents(collection: Collection, query: Dict) -> int:
#     result = collection.delete_many(query)
#     return result.deleted_count

# # Example usage
# if __name__ == "__main__":
#     # Connection details
#     mongodb_host = 'localhost'
#     mongodb_port = 27017
#     database_name = 'mydatabase'
#     collection_name = 'mycollection'

#     # Connect to MongoDB
#     db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

#     # Retrieve a specific collection
#     collection = db[collection_name]

#     # Delete Operation
#     query = {"name": "John Doe"}
#     deleted_count = delete_documents(collection, query)
#     print(f"Deleted {deleted_count} documents")





