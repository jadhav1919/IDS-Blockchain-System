# blockchain.py
import hashlib, json
from datetime import datetime

class Block:
    def __init__(self, index, timestamp, data, prev_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data  # dictionary
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.data, sort_keys=True)}{self.prev_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def to_dict(self):
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "prev_hash": self.prev_hash,
            "hash": self.hash
        }

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, str(datetime.utcnow()), {"msg":"genesis"}, "0")

    def get_latest(self):
        return self.chain[-1]

    def add_block(self, data):
        prev = self.get_latest()
        new_block = Block(len(self.chain), str(datetime.utcnow()), data, prev.hash)
        self.chain.append(new_block)
        return new_block

    def is_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i-1]
            if curr.hash != curr.calculate_hash():
                return False
            if curr.prev_hash != prev.hash:
                return False
        return True

    def to_list(self):
        return [b.to_dict() for b in self.chain]
