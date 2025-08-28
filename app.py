from flask import Flask, jsonify, request
from flask_cors import CORS   # ✅ Import CORS
import json
app = Flask(__name__)
CORS(app)  # ✅ Enable CORS for all routes & origins

# Sample data
data ={}
with open("data.json",'r',encoding='utf-8')as f:
    json.load(f)

# Default response when not found
not_found_obj = {"question": "None found", "answer": "None found"}

# ----------------- Routes -----------------

@app.route('/')
def home():
    return jsonify({"message": "Server running fine"})


@app.route('/number/<num>', methods=['GET'])
def get_by_number(num):
    return jsonify(data.get(num, not_found_obj))


@app.route('/title/<title>', methods=['GET'])
def get_by_title(title):
    for k, v in data.items():
        if title.lower() in v["question"].lower() or title.lower() in v["answer"].lower():
            return jsonify(v)
    return jsonify(not_found_obj)


# ----------------- Run -----------------
if __name__ == '__main__':
    # 0.0.0.0 allows external access (not just localhost)
    app.run(host='0.0.0.0', port=5000, debug=True)
