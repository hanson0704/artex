from pymongo import MongoClient

def get_db():
    # Get database connection and ensure all required collections exist
    client = MongoClient('mongodb://localhost:27017/')
    db = client['art_exhibition_db']

    required = [
        "artworks",
        "artists",
        "critics",
        "visitors",
        "galleries",
        "reviews"
    ]

    # Create collections if missing
    existing = db.list_collection_names()
    for col in required:
        if col not in existing:
            db[col].insert_one({"_init": True})
            db[col].delete_one({"_init": True})

    return db


# Query 1
def query_1():
    db = get_db()
    return list(db.artworks.find({"auctioned": True}, {"_id": 0}))


# Query 2
def query_2():
    db = get_db()
    pipeline = [
        {"$match": {"sold": True}},
        {"$sort": {"price": -1}},
        {"$limit": 1},
        {"$lookup": {
            "from": "artists",
            "localField": "artist_id",
            "foreignField": "artist_id",
            "as": "artist_info"
        }},
        {"$unwind": "$artist_info"},
        {"$project": {
            "_id": 0,
            "artwork_title": "$title",
            "artist_name": "$artist_info.name",
            "artist_id": "$artist_id",
            "price": 1
        }}
    ]
    return list(db.artworks.aggregate(pipeline))


# Query 3
def query_3():
    db = get_db()
    return list(db.critics.find({"reviews_count": {"$gt": 10}}, {"_id": 0}))


# Query 4
def query_4():
    db = get_db()
    pipeline = [
        {"$lookup": {
            "from": "galleries",
            "localField": "gallery_id",
            "foreignField": "gallery_id",
            "as": "gallery_info"
        }},
        {"$unwind": "$gallery_info"},
        {"$lookup": {
            "from": "reviews",
            "localField": "artwork_id",
            "foreignField": "artwork_id",
            "as": "reviews"
        }},
        {"$unwind": "$reviews"},
        {"$group": {
            "_id": "$gallery_info.section",
            "avg_rating": {"$avg": "$reviews.rating"},
            "total_reviews": {"$sum": 1}
        }},
        {"$project": {
            "_id": 0,
            "section": "$_id",
            "avg_rating": {"$round": ["$avg_rating", 2]},
            "total_reviews": 1
        }},
        {"$sort": {"avg_rating": -1}}
    ]
    return list(db.artworks.aggregate(pipeline))


# Query 5
def query_5():
    db = get_db()
    pipeline = [
        {"$group": {"_id": "$theme", "artwork_count": {"$sum": 1}}},
        {"$sort": {"artwork_count": -1}},
        {"$limit": 1},
        {"$project": {"_id": 0, "theme": "$_id", "artwork_count": 1}}
    ]
    return list(db.artworks.aggregate(pipeline))


# Query 6
def query_6():
    db = get_db()
    return list(db.visitors.find({"purchases_count": {"$gt": 2}}, {"_id": 0}))


# Query 7
def query_7():
    db = get_db()
    pipeline = [
        {"$group": {
            "_id": "$artwork_id",
            "has_critic_review": {"$max": {"$cond": [{"$ne": ["$critic_id", None]}, 1, 0]}},
            "has_visitor_review": {"$max": {"$cond": [{"$ne": ["$visitor_id", None]}, 1, 0]}}
        }},
        {"$match": {"has_critic_review": 1, "has_visitor_review": 1}},
        {"$lookup": {
            "from": "artworks",
            "localField": "_id",
            "foreignField": "artwork_id",
            "as": "artwork_info"
        }},
        {"$unwind": "$artwork_info"},
        {"$project": {
            "_id": 0,
            "artwork_id": "$_id",
            "title": "$artwork_info.title",
            "artist_id": "$artwork_info.artist_id",
            "theme": "$artwork_info.theme"
        }}
    ]
    return list(db.reviews.aggregate(pipeline))


# Query 8
def query_8():
    db = get_db()
    pipeline = [
        {"$group": {
            "_id": "$artist_id",
            "galleries": {"$addToSet": "$gallery_id"}
        }},
        {"$match": {"$expr": {"$gt": [{"$size": "$galleries"}, 1]}}},
        {"$lookup": {
            "from": "artists",
            "localField": "_id",
            "foreignField": "artist_id",
            "as": "artist_info"
        }},
        {"$unwind": "$artist_info"},
        {"$project": {
            "_id": 0,
            "artist_id": "$_id",
            "artist_name": "$artist_info.name",
            "gallery_count": {"$size": "$galleries"},
            "galleries": 1
        }}
    ]
    return list(db.artworks.aggregate(pipeline))


# Query 9
def query_9():
    db = get_db()
    return list(db.artworks.find(
        {"$or": [{"sold": False}, {"auctioned": False}]},
        {"_id": 0}
    ))


# Query 10
def query_10():
    db = get_db()
    result = list(
        db.artworks.find({"medium": {"$regex": "Sculpture", "$options": "i"}})
        .sort("price", -1)
        .limit(1)
    )
    for r in result:
        r.pop("_id", None)
    return result


# Query 11
def query_11():
    db = get_db()
    pipeline = [
        {"$match": {"medium": {"$regex": "Painting|Oil|Acrylic|Watercolor", "$options": "i"}}},
        {"$group": {"_id": "$gallery_id", "painting_count": {"$sum": 1}}},
        {"$lookup": {
            "from": "galleries",
            "localField": "_id",
            "foreignField": "gallery_id",
            "as": "gallery_info"
        }},
        {"$unwind": "$gallery_info"},
        {"$project": {
            "_id": 0,
            "gallery_id": "$_id",
            "gallery_name": "$gallery_info.name",
            "section": "$gallery_info.section",
            "painting_count": 1
        }},
        {"$sort": {"painting_count": -1}},
        {"$limit": 1}
    ]
    return list(db.artworks.aggregate(pipeline))


# Query 12
def query_12():
    db = get_db()
    return list(db.artists.find({}, {"_id": 0}).sort("avg_rating", -1).limit(3))


# Query Dictionary (used by CLI)
QUERIES = {
    1: query_1,
    2: query_2,
    3: query_3,
    4: query_4,
    5: query_5,
    6: query_6,
    7: query_7,
    8: query_8,
    9: query_9,
    10: query_10,
    11: query_11,
    12: query_12,
}

QUERY_DESCRIPTIONS = {
    1: "List artworks that were auctioned",
    2: "Find the artist whose artwork sold for the highest price",
    3: "Show critics who reviewed more than 10 artworks",
    4: "Calculate the average rating given per gallery section",
    5: "Identify themes with the maximum number of artworks",
    6: "Retrieve visitors who purchased more than 2 artworks",
    7: "Find artworks reviewed by both critics and visitors",
    8: "Show artists who displayed works in multiple galleries",
    9: "Identify artworks not sold or auctioned",
    10: "Find the most expensive sculpture exhibited",
    11: "Show galleries with the highest number of paintings",
    12: "Retrieve top 3 highest-rated artists",
}
