"""
Art Exhibition Database Setup
Run this file once to create database, collections, and insert sample data
Usage: python setup_database.py
"""

from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['art_exhibition_db']

# Clear existing collections
print("Clearing existing collections...")
db.artists.delete_many({})
db.artworks.delete_many({})
db.galleries.delete_many({})
db.visitors.delete_many({})
db.critics.delete_many({})
db.reviews.delete_many({})
db.auctions.delete_many({})
db.purchases.delete_many({})

print("Inserting sample data...")

# Insert Artists (NU25MCA36-42)
artists = [
    {"artist_id": "NU25MCA36", "name": "Rajesh Kumar", "specialty": "Oil Painting", "total_artworks": 5, "avg_rating": 4.5},
    {"artist_id": "NU25MCA37", "name": "Priya Sharma", "specialty": "Sculpture", "total_artworks": 3, "avg_rating": 4.8},
    {"artist_id": "NU25MCA38", "name": "Amit Patel", "specialty": "Installation", "total_artworks": 4, "avg_rating": 4.2},
    {"artist_id": "NU25MCA39", "name": "Sneha Reddy", "specialty": "Abstract Art", "total_artworks": 6, "avg_rating": 4.7},
    {"artist_id": "NU25MCA40", "name": "Vikram Singh", "specialty": "Photography", "total_artworks": 4, "avg_rating": 4.3},
    {"artist_id": "NU25MCA41", "name": "Meera Joshi", "specialty": "Watercolor", "total_artworks": 5, "avg_rating": 4.6},
    {"artist_id": "NU25MCA42", "name": "Arjun Desai", "specialty": "Mixed Media", "total_artworks": 3, "avg_rating": 4.9}
]
db.artists.insert_many(artists)

# Insert Galleries
galleries = [
    {"gallery_id": "G001", "name": "Modern Art Gallery", "section": "Contemporary", "artworks_count": 8},
    {"gallery_id": "G002", "name": "Classical Arts Center", "section": "Traditional", "artworks_count": 6},
    {"gallery_id": "G003", "name": "Sculpture Pavilion", "section": "3D Art", "artworks_count": 5},
    {"gallery_id": "G004", "name": "Abstract Expressions", "section": "Contemporary", "artworks_count": 7}
]
db.galleries.insert_many(galleries)

# Insert Artworks
artworks = [
    {"artwork_id": "AW001", "title": "Sunset Dreams", "artist_id": "NU25MCA36", "theme": "Nature", "medium": "Oil on Canvas", "price": 50000, "gallery_id": "G001", "auctioned": True, "sold": True},
    {"artwork_id": "AW002", "title": "Urban Chaos", "artist_id": "NU25MCA36", "theme": "Urban Life", "medium": "Acrylic", "price": 35000, "gallery_id": "G001", "auctioned": False, "sold": True},
    {"artwork_id": "AW003", "title": "Eternal Beauty", "artist_id": "NU25MCA37", "theme": "Human Form", "medium": "Bronze Sculpture", "price": 150000, "gallery_id": "G003", "auctioned": True, "sold": True},
    {"artwork_id": "AW004", "title": "Freedom", "artist_id": "NU25MCA37", "theme": "Abstract", "medium": "Marble Sculpture", "price": 200000, "gallery_id": "G003", "auctioned": True, "sold": True},
    {"artwork_id": "AW005", "title": "Digital Dreams", "artist_id": "NU25MCA38", "theme": "Technology", "medium": "Installation", "price": 80000, "gallery_id": "G001", "auctioned": False, "sold": False},
    {"artwork_id": "AW006", "title": "Colors of Life", "artist_id": "NU25MCA39", "theme": "Abstract", "medium": "Mixed Media", "price": 45000, "gallery_id": "G004", "auctioned": True, "sold": True},
    {"artwork_id": "AW007", "title": "Silent Whispers", "artist_id": "NU25MCA39", "theme": "Nature", "medium": "Oil Painting", "price": 60000, "gallery_id": "G004", "auctioned": False, "sold": False},
    {"artwork_id": "AW008", "title": "Moments Captured", "artist_id": "NU25MCA40", "theme": "Portrait", "medium": "Photography", "price": 25000, "gallery_id": "G002", "auctioned": False, "sold": True},
    {"artwork_id": "AW009", "title": "Flowing Waters", "artist_id": "NU25MCA41", "theme": "Nature", "medium": "Watercolor", "price": 30000, "gallery_id": "G002", "auctioned": True, "sold": False},
    {"artwork_id": "AW010", "title": "The Guardian", "artist_id": "NU25MCA37", "theme": "Mythology", "medium": "Stone Sculpture", "price": 180000, "gallery_id": "G003", "auctioned": False, "sold": False},
    {"artwork_id": "AW011", "title": "Cosmic Dance", "artist_id": "NU25MCA42", "theme": "Abstract", "medium": "Mixed Media", "price": 95000, "gallery_id": "G004", "auctioned": True, "sold": True},
    {"artwork_id": "AW012", "title": "Mountain Majesty", "artist_id": "NU25MCA36", "theme": "Nature", "medium": "Oil Painting", "price": 55000, "gallery_id": "G001", "auctioned": False, "sold": False}
]
db.artworks.insert_many(artworks)

# Insert Critics
critics = [
    {"critic_id": "C001", "name": "Dr. Ramesh Iyer", "expertise": "Contemporary Art", "reviews_count": 15},
    {"critic_id": "C002", "name": "Anjali Menon", "expertise": "Sculpture", "reviews_count": 12},
    {"critic_id": "C003", "name": "Suresh Kumar", "expertise": "Classical Art", "reviews_count": 8},
    {"critic_id": "C004", "name": "Kavita Nair", "expertise": "Modern Art", "reviews_count": 11}
]
db.critics.insert_many(critics)

# Insert Visitors
visitors = [
    {"visitor_id": "V001", "name": "Rohit Sharma", "email": "rohit@email.com", "purchases_count": 3},
    {"visitor_id": "V002", "name": "Anita Desai", "email": "anita@email.com", "purchases_count": 1},
    {"visitor_id": "V003", "name": "Karan Mehta", "email": "karan@email.com", "purchases_count": 4},
    {"visitor_id": "V004", "name": "Pooja Singh", "email": "pooja@email.com", "purchases_count": 2},
    {"visitor_id": "V005", "name": "Deepak Rao", "email": "deepak@email.com", "purchases_count": 0}
]
db.visitors.insert_many(visitors)

# Insert Reviews
reviews = [
    {"review_id": "R001", "artwork_id": "AW001", "critic_id": "C001", "rating": 4.5, "comment": "Stunning use of colors", "visitor_id": "V001"},
    {"review_id": "R002", "artwork_id": "AW001", "critic_id": None, "rating": 4.0, "comment": "Beautiful piece", "visitor_id": "V001"},
    {"review_id": "R003", "artwork_id": "AW003", "critic_id": "C002", "rating": 5.0, "comment": "Masterpiece in bronze", "visitor_id": "V003"},
    {"review_id": "R004", "artwork_id": "AW003", "critic_id": None, "rating": 4.8, "comment": "Incredible detail", "visitor_id": "V004"},
    {"review_id": "R005", "artwork_id": "AW004", "critic_id": "C002", "rating": 4.9, "comment": "Exceptional craftsmanship", "visitor_id": None},
    {"review_id": "R006", "artwork_id": "AW006", "critic_id": "C001", "rating": 4.3, "comment": "Vibrant and alive", "visitor_id": "V002"},
    {"review_id": "R007", "artwork_id": "AW006", "critic_id": None, "rating": 4.5, "comment": "Love the energy", "visitor_id": "V002"},
    {"review_id": "R008", "artwork_id": "AW011", "critic_id": "C004", "rating": 4.8, "comment": "Innovative approach", "visitor_id": "V003"},
    {"review_id": "R009", "artwork_id": "AW002", "critic_id": "C001", "rating": 4.2, "comment": "Good composition", "visitor_id": None},
    {"review_id": "R010", "artwork_id": "AW008", "critic_id": "C004", "rating": 4.0, "comment": "Well captured moments", "visitor_id": "V001"}
]
db.reviews.insert_many(reviews)

# Insert Auctions
auctions = [
    {"auction_id": "AU001", "artwork_id": "AW001", "final_price": 50000, "buyer_id": "V001", "auction_date": datetime(2024, 11, 15)},
    {"auction_id": "AU002", "artwork_id": "AW003", "final_price": 150000, "buyer_id": "V003", "auction_date": datetime(2024, 11, 16)},
    {"auction_id": "AU003", "artwork_id": "AW004", "final_price": 200000, "buyer_id": "V003", "auction_date": datetime(2024, 11, 17)},
    {"auction_id": "AU004", "artwork_id": "AW006", "final_price": 45000, "buyer_id": "V002", "auction_date": datetime(2024, 11, 18)},
    {"auction_id": "AU005", "artwork_id": "AW009", "final_price": 30000, "buyer_id": None, "auction_date": datetime(2024, 11, 20)},
    {"auction_id": "AU006", "artwork_id": "AW011", "final_price": 95000, "buyer_id": "V004", "auction_date": datetime(2024, 11, 21)}
]
db.auctions.insert_many(auctions)

# Insert Purchases
purchases = [
    {"purchase_id": "P001", "artwork_id": "AW001", "visitor_id": "V001", "price": 50000, "purchase_date": datetime(2024, 11, 15)},
    {"purchase_id": "P002", "artwork_id": "AW002", "visitor_id": "V001", "price": 35000, "purchase_date": datetime(2024, 11, 16)},
    {"purchase_id": "P003", "artwork_id": "AW003", "visitor_id": "V003", "price": 150000, "purchase_date": datetime(2024, 11, 17)},
    {"purchase_id": "P004", "artwork_id": "AW004", "visitor_id": "V003", "price": 200000, "purchase_date": datetime(2024, 11, 18)},
    {"purchase_id": "P005", "artwork_id": "AW006", "visitor_id": "V002", "price": 45000, "purchase_date": datetime(2024, 11, 19)},
    {"purchase_id": "P006", "artwork_id": "AW008", "visitor_id": "V001", "price": 25000, "purchase_date": datetime(2024, 11, 20)},
    {"purchase_id": "P007", "artwork_id": "AW011", "visitor_id": "V004", "price": 95000, "purchase_date": datetime(2024, 11, 21)},
    {"purchase_id": "P008", "artwork_id": "AW011", "visitor_id": "V003", "price": 95000, "purchase_date": datetime(2024, 11, 21)},
    {"purchase_id": "P009", "artwork_id": "AW001", "visitor_id": "V004", "price": 50000, "purchase_date": datetime(2024, 11, 22)}
]
db.purchases.insert_many(purchases)

print("\n✅ Database setup completed successfully!")
print("\n📊 Collections created:")
print(f"   - Artists: {db.artists.count_documents({})}")
print(f"   - Artworks: {db.artworks.count_documents({})}")
print(f"   - Galleries: {db.galleries.count_documents({})}")
print(f"   - Visitors: {db.visitors.count_documents({})}")
print(f"   - Critics: {db.critics.count_documents({})}")
print(f"   - Reviews: {db.reviews.count_documents({})}")
print(f"   - Auctions: {db.auctions.count_documents({})}")
print(f"   - Purchases: {db.purchases.count_documents({})}")

print("\n🎨 You can now:")
print("   1. Open MongoDB Compass and connect to localhost:27017")
print("   2. Run queries using: python cli.py --query <number>")
print("   3. Start API server: python api.py")
print("   4. Open index.html in browser")

client.close()