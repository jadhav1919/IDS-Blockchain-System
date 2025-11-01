from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Simple in-memory blockchain
blockchain = []

# Genesis block
genesis_block = {
    "index": 1,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "data": "Genesis Block",
    "previous_hash": "0",
    "hash": "GENESIS_HASH"
}
blockchain.append(genesis_block)


@app.route('/')
def home():
    return jsonify({"message": "✅ Blockchain Server Running", "total_blocks": len(blockchain)})


@app.route('/add_block', methods=['POST'])
def add_block():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid block data"}), 400

    blockchain.append(data)
    print(f"🧱 Block Added → Index {data.get('index')} | {data.get('data')}")
    return jsonify({"message": "Block added successfully", "total_blocks": len(blockchain)}), 200


@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify(blockchain), 200


if __name__ == "__main__":
    print("🔗 Starting Blockchain Core on http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000)
