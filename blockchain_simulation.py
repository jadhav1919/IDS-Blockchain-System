import hashlib
import json
import time
from datetime import datetime

# -----------------------------
# Step 1: Define a Block class
# -----------------------------
class Block:
    def __init__(self, index, timestamp, data, prev_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data  # e.g., attack details
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.prev_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

# -----------------------------
# Step 2: Define the Blockchain
# -----------------------------
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, str(datetime.now()), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_data):
        prev_block = self.get_latest_block()
        new_block = Block(
            len(self.chain),
            str(datetime.now()),
            new_data,
            prev_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]
            if curr.hash != curr.calculate_hash():
                return False
            if curr.prev_hash != prev.hash:
                return False
        return True

# -----------------------------
# Step 3: Simulate IDS results being added
# -----------------------------
if __name__ == "__main__":
    # Create blockchain instance
    bc = Blockchain()

    # Simulate alerts from IDS nodes
    detections = [
        {"Node": "RSP1", "PacketID": 1, "Prediction": "Attack Detected"},
        {"Node": "RSP2", "PacketID": 2, "Prediction": "Normal"},
        {"Node": "RSP3", "PacketID": 3, "Prediction": "Attack Detected"},
    ]

    print("\n🧱 Adding IDS alerts to Blockchain...\n")
    for d in detections:
        bc.add_block(json.dumps(d))
        print(f"✅ Block {len(bc.chain)-1} added: {d}")

    print("\n📜 Final Blockchain Ledger:\n")
    for block in bc.chain:
        print(json.dumps(block.__dict__, indent=4))

    print("\n🔒 Chain Validity:", bc.is_chain_valid())
