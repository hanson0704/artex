const API_URL = "http://localhost:5000";

/* ============================================
   QUERY EXECUTION
=============================================== */

async function executeQuery(queryNumber) {
  const resultsContent = document.getElementById("resultsContent");
  const resultsTitle = document.getElementById("resultsTitle");
  const resultCount = document.getElementById("resultCount");

  resultsContent.innerHTML = `
        <div class="loading">
            <div class="spinner"></div>
            <p>Loading results...</p>
        </div>
    `;

  try {
    const response = await fetch(`${API_URL}/query/${queryNumber}`);
    if (!response.ok) throw new Error("HTTP Error: " + response.status);

    const data = await response.json();

    resultsTitle.textContent = `Query ${queryNumber} Results`;
    resultCount.textContent = `${data.count} result${
      data.count !== 1 ? "s" : ""
    }`;

    if (data.results.length > 0) {
      resultsContent.innerHTML = data.results
        .map((item, i) => formatResultCard(item, i + 1))
        .join("");
    } else {
      resultsContent.innerHTML = `<div class="no-results">No results found.</div>`;
    }
  } catch (error) {
    resultsContent.innerHTML = `
            <div class="error">
                <strong>Error:</strong> ${error.message}<br><br>
                Make sure:<br>
                1️⃣ MongoDB is running<br>
                2️⃣ API: <code>python api.py</code><br>
                3️⃣ DB initialized: <code>python setup_database.py</code>
            </div>
        `;
  }
}

/* ============================================
   FORMAT RESULT CARD
=============================================== */

function formatResultCard(item, index) {
  let html = `<div class="result-card"><h3 style="color:#667eea;">Result ${index}</h3>`;

  for (let [key, value] of Object.entries(item)) {
    if (key === "_id") continue;

    let displayValue = value;

    if (key === "sold" || key === "auctioned") {
      displayValue = value
        ? `<span class="status-badge status-sold">Yes</span>`
        : `<span class="status-badge status-available">No</span>`;
    }

    html += `<div><strong>${key}:</strong> ${displayValue}</div>`;
  }

  html += "</div>";
  return html;
}

/* ============================================
   SCHEMA DEFINITIONS FOR INSERT MODAL
=============================================== */

const SCHEMAS = {
  artists: ["artist_id", "name", "specialty", "total_artworks", "avg_rating"],
  artworks: [
    "artwork_id",
    "title",
    "artist_id",
    "theme",
    "medium",
    "price",
    "gallery_id",
    "auctioned",
    "sold",
  ],
  galleries: ["gallery_id", "name", "section", "artworks_count"],
  critics: ["critic_id", "name", "expertise", "reviews_count"],
  visitors: ["visitor_id", "name", "email", "purchases_count"],
  reviews: [
    "review_id",
    "artwork_id",
    "critic_id",
    "rating",
    "comment",
    "visitor_id",
  ],
  auctions: [
    "auction_id",
    "artwork_id",
    "final_price",
    "buyer_id",
    "auction_date",
  ],
  purchases: [
    "purchase_id",
    "artwork_id",
    "visitor_id",
    "price",
    "purchase_date",
  ],
};

/* ============================================
   POPUP INSERT MODAL LOGIC
=============================================== */

function showInsertPanel() {
  document.getElementById("insertModal").style.display = "flex";
}

function closeInsertModal() {
  document.getElementById("insertModal").style.display = "none";
  document.getElementById("insertForm").innerHTML = "";
  document.getElementById("collectionSelect").selectedIndex = 0;
}

function loadInsertFields() {
  const collection = document.getElementById("collectionSelect").value;
  const form = document.getElementById("insertForm");
  form.innerHTML = "";

  if (!collection) return;

  SCHEMAS[collection].forEach((field) => {
    form.innerHTML += `
            <label><strong>${field}</strong></label>
            <input type="text" id="${field}" class="modal-field">
        `;
  });
}

async function submitInsert() {
  const collection = document.getElementById("collectionSelect").value;
  if (!collection) {
    alert("Please select a collection!");
    return;
  }

  let record = {};
  let emptyFields = [];

  SCHEMAS[collection].forEach((field) => {
    let value = document.getElementById(field).value.trim();

    if (value === "") {
      emptyFields.push(field);
      document.getElementById(field).style.border = "2px solid red";
    } else {
      document.getElementById(field).style.border = "1px solid #ccc";
    }

    record[field] = value;
  });

  // Stop submission if any field is empty
  if (emptyFields.length > 0) {
    alert("❗Please fill all fields.\nMissing: " + emptyFields.join(", "));
    return;
  }

  const response = await fetch(`${API_URL}/insert/${collection}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(record),
  });

  const data = await response.json();
  alert(data.message || data.error);

  closeInsertModal();
}

/* ============================================
   DELETE MODAL LOGIC
=============================================== */

function showDeletePanel() {
  document.getElementById("deleteModal").style.display = "flex";
}

function closeDeleteModal() {
  document.getElementById("deleteModal").style.display = "none";
  document.getElementById("deleteForm").innerHTML = "";
  document.getElementById("deleteCollectionSelect").selectedIndex = 0;
}

function loadDeleteField() {
  const collection = document.getElementById("deleteCollectionSelect").value;
  const form = document.getElementById("deleteForm");

  form.innerHTML = "";

  if (!collection) return;

  // ID names depend on collection
  const ID_FIELDS = {
    artists: "artist_id",
    artworks: "artwork_id",
    galleries: "gallery_id",
    critics: "critic_id",
    visitors: "visitor_id",
    reviews: "review_id",
    auctions: "auction_id",
    purchases: "purchase_id",
  };

  form.innerHTML = `
        <label><strong>${ID_FIELDS[collection]}</strong></label>
        <input type="text" id="deleteIdInput" class="modal-field">
    `;
}
async function submitDelete() {
  const collection = document.getElementById("deleteCollectionSelect").value;
  const recordId = document.getElementById("deleteIdInput")?.value.trim();

  if (!collection) {
    alert("Please select a collection!");
    return;
  }

  if (!recordId) {
    alert("Please enter a valid ID!");
    document.getElementById("deleteIdInput").style.border = "2px solid red";
    return;
  }

  document.getElementById("deleteIdInput").style.border = "1px solid #ccc";

  const response = await fetch(`${API_URL}/delete/${collection}/${recordId}`, {
    method: "DELETE",
  });

  const data = await response.json();
  alert(data.message || data.error);

  closeDeleteModal();
}
