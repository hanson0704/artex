from pymongo import MongoClient

# Local MongoDB connection URI
MONGO_URI = "mongodb://localhost:27017/"

# Your database and collection names
DB_NAME = "ArtExhibitionDB"
COLLECTION_NAME = "Artworks"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]
