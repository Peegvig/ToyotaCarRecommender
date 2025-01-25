from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MongoDB URI from environment variables
mongo_uri = os.getenv("MONGO_URI")

# Connect to MongoDB Atlas
try:
    client = MongoClient(mongo_uri)
    db = client["car_recommendations"]
    cars_collection = db["cars"]

    # Insert a test document
    test_car = {"name": "Toyota Tacoma", "price": 40000, "features": ["4WD", "Off-road package"]}
    cars_collection.insert_one(test_car)

    # Retrieve the document
    retrieved_car = cars_collection.find_one({"name": "Toyota Tacoma"})
    print("MongoDB Connection Successful!")
    print("Retrieved Car:", retrieved_car)

except Exception as e:
    print("Error connecting to MongoDB:", e)
