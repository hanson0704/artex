# 🎨 ARTEX – Art Exhibition Database Management System

## 📌 Overview

ARTEX is a database-driven system designed to manage information related to art exhibitions.
The system stores and retrieves data about **artists, artworks, galleries, critics, visitors, reviews, purchases, and auctions**.

It provides both:

* 🌐 Web Interface
* 💻 Command Line Interface (CLI)

The project demonstrates a **full-stack implementation using Python, MongoDB, and a web frontend**.

---

## 🛠 Technologies Used

### ⚙️ Backend

* 🐍 Python
* 🌶 Flask Framework
* 🔗 PyMongo

### 🗄 Database

* 🍃 MongoDB (NoSQL Database)

### 🎨 Frontend

* 🧱 HTML
* 🎨 CSS
* ⚡ JavaScript (Fetch API)

---

## 🏗 System Architecture

### ⚙️ Backend

The backend handles:

* API request handling
* Database query execution
* Input validation
* JSON response generation
* CLI operations for inserting and deleting records

Example API endpoints:

```id="api01"
/query/<number>
/insert/<collection>
/delete/<collection>/<id>
```

---

### 🗄 Database

MongoDB is used because of:

* Flexible schema
* JSON-style documents
* Fast queries and aggregation
* Easy integration with Python

Collections used:

* artists
* artworks
* galleries
* critics
* visitors
* reviews
* purchases
* auctions

The script `setup_database.py` initializes collections and inserts sample data. 

---

### 🎨 Frontend

The frontend provides an interactive user interface.

Features include:

* 📊 Interactive query panel
* 🪟 Animated modal forms
* ➕ Insert operations
* ❌ Delete operations
* ⚡ Real-time results using JavaScript

---

## 💻 Command Line Interface (CLI)

The CLI tool (`cli.py`) allows:

* Running queries directly
* Inserting documents interactively
* Deleting records using custom ID fields

Example:

```id="cli01"
python cli.py
```

---

## 📁 Project Structure

```id="struct01"
ARTEX
│
├── backend
│   ├── api.py
│   ├── cli.py
│   ├── db.py
│   ├── queries.py
│   └── setup_database.py
│
├── frontend
│   ├── index.html
│   ├── script.js
│   └── styles.css
│
└── .gitignore
```

---

## 🔎 Sample Queries Implemented

The system supports several database queries including:

1️⃣ List artworks that were auctioned
2️⃣ Find the artist whose artwork sold for the highest price
3️⃣ Show critics who reviewed more than 10 artworks
4️⃣ Calculate average rating per gallery section
5️⃣ Identify themes with the maximum number of artworks
6️⃣ Retrieve visitors who purchased more than two artworks
7️⃣ Find artworks reviewed by both critics and visitors
8️⃣ Show artists who displayed works in multiple galleries
9️⃣ Identify artworks not sold or not auctioned
🔟 Find the most expensive sculpture exhibited
1️⃣1️⃣ Show galleries with the highest number of paintings
1️⃣2️⃣ Retrieve the top 3 highest-rated artists 

---

## ⚡ Setup Instructions

### 1️⃣ Clone the Repository

```id="setup01"
git clone https://github.com/yourusername/artex.git
cd artex
```

### 2️⃣ Install Dependencies

```id="setup02"
pip install flask pymongo
```

### 3️⃣ Setup Database

```id="setup03"
python backend/setup_database.py
```

### 4️⃣ Run Backend Server

```id="setup04"
python backend/api.py
```

### 5️⃣ Open Frontend

Open:

```
frontend/index.html
```

in your browser.

---

## 👨‍💻 Authors

* G Anup
* Gaurav S K
* Goutam Prakash Hegde
* Gowrav G Shetty
* Hanson Vaz
* Harsha S Kotian

🎓 Master of Computer Applications
🏫 Nitte (Deemed to be University)
