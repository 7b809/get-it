from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# ✅ Load data.json
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

not_found_obj = {"question": "None found", "answer": "None found"}

@app.route("/")
def home():
    return jsonify({"message": "Server running fine"})

@app.route("/number/<num>")
def get_by_number(num):
    return jsonify(data.get(num, not_found_obj))

@app.route("/title/<title>")
def get_by_title(title):
    for _, v in data.items():
        if title.lower() in v["question"].lower() or title.lower() in v["answer"].lower():
            return jsonify(v)
    return jsonify(not_found_obj)

# ✅ Vercel requires app as "app"
# Do NOT call app.run() here
