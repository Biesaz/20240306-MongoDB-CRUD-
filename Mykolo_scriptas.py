from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict
from faker import Faker
from random import randint


def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
    client = MongoClient(host, port)
    database = client[db_name]
    return database


def insert_document(collection: Collection, document: Dict) -> str:
    result = collection.insert_one(document)
    print(f"Printed result: {result}")
    return str(result.inserted_id)


def create_a_person():
    fake = Faker()
    name = fake.first_name()
    surname = fake.last_name()
    age = randint(18, 75)
    years_employed = (
        -1
    )  # Cannot use zero, as it is a valid value, can't use None, as it wont work
    while age - 18 < years_employed or years_employed == -1:
        years_employed = randint(0, 55)
    return name, surname, age, years_employed

if __name__ == "__main__":
    mongodb_host = "localhost"
    mongodb_port = 27017
    database_name = "people"
    collection_name = "employees"

    db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

    collection = db[collection_name]
    fake = Faker()
    for _ in range(10):
        name, surname, age, years_employed = create_a_person()
        document = {
            "name": name,
            "surname": surname,
            "age": age,
            "years_employed": years_employed,
        }
        inserted_id = insert_document(collection, document)
        print(f"Inserted document with ID: {inserted_id}")
        print(f"This person was inserted into the database: {document}")
