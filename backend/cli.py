"""
Command Line Interface for Art Exhibition Queries
Usage:
    python cli.py --query <number>
    python cli.py --insert
    python cli.py --delete
"""

import argparse
import json
from queries import QUERIES, QUERY_DESCRIPTIONS, get_db


# ID FIELDS MUST ALWAYS BE STRING
ID_FIELDS = [
    "artist_id", "artwork_id", "gallery_id", "critic_id",
    "visitor_id", "review_id", "purchase_id", "auction_id"
]


# Schema definitions for each collection
SCHEMAS = {
    "artworks": [
        "artwork_id", "title", "artist_id", "gallery_id", "theme",
        "medium", "price", "sold", "auctioned"
    ],
    "artists": [
        "artist_id", "name", "specialty", "total_artworks", "avg_rating"
    ],
    "critics": [
        "critic_id", "name", "expertise", "reviews_count"
    ],
    "visitors": [
        "visitor_id", "name", "email", "purchases_count"
    ],
    "galleries": [
        "gallery_id", "name", "section", "artworks_count"
    ],
    "reviews": [
        "review_id", "artwork_id", "critic_id", "visitor_id", "rating", "comment"
    ],
    "purchases": [
        "purchase_id", "artwork_id", "visitor_id", "price", "purchase_date"
    ],
    "auctions": [
        "auction_id", "artwork_id", "final_price", "buyer_id", "auction_date"
    ]
}


def ensure_collections_exist(db):
    required = [
        "artworks", "artists", "critics", "visitors",
        "galleries", "reviews", "purchases", "auctions"
    ]

    for col in required:
        if col not in db.list_collection_names():
            db[col].insert_one({"_temp": True})
            db[col].delete_one({"_temp": True})


def format_output(data):
    if not data:
        return "No results found."
    return json.dumps(data, indent=2, default=str)


def convert_value(value):
    """Convert numeric values automatically, except for ID fields."""
    if value.isdigit():
        return int(value)
    try:
        return float(value)
    except:
        return value


# -------------------------------------------------------------
# INSERT DATA
# -------------------------------------------------------------

def insert_data():
    db = get_db()
    ensure_collections_exist(db)

    print("\nINSERT NEW RECORD")
    print("-" * 50)

    available = list(SCHEMAS.keys())
    print("Available collections:", ", ".join(available))

    collection_name = input("\nEnter collection name: ").strip()

    if collection_name not in SCHEMAS:
        print("❌ Invalid or unsupported collection name!")
        return

    fields = SCHEMAS[collection_name]

    data = {}

    for field in fields:
        value = input(f"{field}: ").strip()

        if value == "":
            data[field] = None
            continue

        # ID fields must remain STRING
        if field in ID_FIELDS:
            data[field] = value
        else:
            data[field] = convert_value(value)

    result = db[collection_name].insert_one(data)
    print(f"\n✅ Inserted successfully with ID: {result.inserted_id}")


# -------------------------------------------------------------
# DELETE DATA
# -------------------------------------------------------------

def delete_interactive():
    db = get_db()
    ensure_collections_exist(db)

    print("\nDELETE RECORD")
    print("-" * 50)

    available = list(SCHEMAS.keys())
    print("Available collections:", ", ".join(available))

    collection_name = input("\nEnter collection name: ").strip()

    if collection_name not in SCHEMAS:
        print("❌ Invalid or unsupported collection name!")
        return

    id_fields = {
        "artworks": "artwork_id",
        "artists": "artist_id",
        "critics": "critic_id",
        "visitors": "visitor_id",
        "galleries": "gallery_id",
        "reviews": "review_id",
        "purchases": "purchase_id",
        "auctions": "auction_id"
    }

    key_field = id_fields[collection_name]

    print(f"\nID Field for {collection_name}: {key_field}")
    record_id = input(f"Enter {key_field}: ").strip()

    if not record_id:
        print("❌ ID cannot be empty!")
        return

    # Always treat ID as STRING
    record_id = str(record_id)

    result = db[collection_name].delete_one({key_field: record_id})

    if result.deleted_count == 1:
        print(f"\n🗑️ Successfully deleted {key_field} = '{record_id}' from {collection_name}")
    else:
        print(f"\n❌ No record found with ID {key_field} = '{record_id}'")


# -------------------------------------------------------------
# MAIN
# -------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Art Exhibition Database Query Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('--query', type=int, choices=range(1, 13), help='Execute query (1–12)')
    parser.add_argument('--list', action='store_true', help='List all available queries')
    parser.add_argument('--insert', action='store_true', help='Insert a new document')
    parser.add_argument('--delete', action='store_true', help='Delete a document interactively')

    args = parser.parse_args()

    if args.list:
        print("\nAVAILABLE QUERIES")
        print("=" * 60)
        for num, desc in QUERY_DESCRIPTIONS.items():
            print(f"{num:2d}. {desc}")
        print("=" * 60)
        return

    if args.insert:
        insert_data()
        return

    if args.delete:
        delete_interactive()
        return

    if args.query:
        q = args.query
        print(f"\nExecuting Query {q}: {QUERY_DESCRIPTIONS[q]}")
        print("=" * 60)

        try:
            results = QUERIES[q]()
            print(format_output(results))
            print("=" * 60)
            print(f"Completed. {len(results)} result(s).")
        except Exception as e:
            print(f"Error executing query: {e}")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
