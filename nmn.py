# Import PyMongo library
from pymongo import MongoClient

# Connection URL for MongoDB
mongo_url = "mongodb://localhost:27017/"

# Connect to MongoDB
client = MongoClient(mongo_url)

# Create or select a database
database_name = "mydatabase"
db = client[database_name]

# Create or select a collection
collection_name = "mycollection"
collection = db[collection_name]

# Insert multiple documents into the collection
data_to_insert = [
    {"name": "John", "age": 25, "city": "New York"},
    {"name": "Alice", "age": 30, "city": "London"},
    {"name": "Bob", "age": 22, "city": "Tokyo"}
]

# Insert data into the collection
result = collection.insert_many(data_to_insert)
print(f"{len(result.inserted_ids)} documents inserted.")

# Query and display documents
print("\nQuerying and displaying documents:")
cursor = collection.find({})

for document in cursor:
    print(document)

# Close the MongoDB connection
client.close()