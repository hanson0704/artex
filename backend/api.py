"""
Flask API Server for Art Exhibition Queries
Start server: python api.py
Server runs on: http://localhost:5000
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from queries import QUERIES, QUERY_DESCRIPTIONS
from queries import QUERIES, QUERY_DESCRIPTIONS, get_db
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

@app.route('/')
def home():
    return jsonify({
        "message": "Art Exhibition API",
        "endpoints": {
            "/queries": "GET - List all available queries",
            "/query/<number>": "GET - Execute a specific query (1-12)"
        }
    })

@app.route('/queries', methods=['GET'])
def list_queries():
    """List all available queries"""
    queries_list = [
        {"number": num, "description": desc}
        for num, desc in QUERY_DESCRIPTIONS.items()
    ]
    return jsonify(queries_list)

@app.route('/query/<int:query_num>', methods=['GET'])
def execute_query(query_num):
    """Execute a specific query"""
    if query_num not in QUERIES:
        return jsonify({
            "error": "Invalid query number",
            "message": f"Query number must be between 1 and 12"
        }), 400
    
    try:
        query_func = QUERIES[query_num]
        results = query_func()
        
        return jsonify({
            "query_number": query_num,
            "description": QUERY_DESCRIPTIONS[query_num],
            "results": json.loads(json.dumps(results, default=str)),
            "count": len(results)
        })
    except Exception as e:
        return jsonify({
            "error": "Query execution failed",
            "message": str(e)
        }), 500

@app.route('/insert/<collection>', methods=['POST'])
def insert_record(collection):
    db = get_db()

    SCHEMAS = {
        "artists": ["artist_id", "name", "specialty", "total_artworks", "avg_rating"],
        "artworks": ["artwork_id", "title", "artist_id", "theme", "medium", "price", "gallery_id", "auctioned", "sold"],
        "galleries": ["gallery_id", "name", "section", "artworks_count"],
        "critics": ["critic_id", "name", "expertise", "reviews_count"],
        "visitors": ["visitor_id", "name", "email", "purchases_count"],
        "reviews": ["review_id", "artwork_id", "critic_id", "rating", "comment", "visitor_id"],
        "auctions": ["auction_id", "artwork_id", "final_price", "buyer_id", "auction_date"],
        "purchases": ["purchase_id", "artwork_id", "visitor_id", "price", "purchase_date"]
    }

    if collection not in SCHEMAS:
        return jsonify({"error": "Invalid collection"}), 400

    data = request.json

    # Convert numbers & booleans automatically
    for key in data:
        if data[key] == "":
            data[key] = None
        elif isinstance(data[key], str) and data[key].isdigit():
            data[key] = int(data[key])
        elif data[key] in ["true", "True", True]:
            data[key] = True
        elif data[key] in ["false", "False", False]:
            data[key] = False

    try:
        db[collection].insert_one(data)
        return jsonify({"message": f"Inserted into {collection} successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/delete/<collection>/<record_id>', methods=['DELETE'])
def delete_record(collection, record_id):
    db = get_db()

    ID_FIELDS = {
        "artists": "artist_id",
        "artworks": "artwork_id",
        "galleries": "gallery_id",
        "critics": "critic_id",
        "visitors": "visitor_id",
        "reviews": "review_id",
        "auctions": "auction_id",
        "purchases": "purchase_id"
    }

    if collection not in ID_FIELDS:
        return jsonify({"error": "Invalid collection"}), 400

    key_field = ID_FIELDS[collection]

    result = db[collection].delete_one({key_field: record_id})

    if result.deleted_count == 1:
        return jsonify({"message": f"Deleted record from {collection} where {key_field}={record_id}"})
    else:
        return jsonify({"error": "Record not found"}), 404



if __name__ == '__main__':
    print("\n🚀 Starting Art Exhibition API Server...")
    print("=" * 70)
    print("Server running on: http://localhost:5000")
    print("=" * 70)
    print("\nAvailable endpoints:")
    print("  GET  /              - API information")
    print("  GET  /queries       - List all queries")
    print("  GET  /query/<num>   - Execute query (1-12)")
    print("\nPress CTRL+C to stop the server\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)