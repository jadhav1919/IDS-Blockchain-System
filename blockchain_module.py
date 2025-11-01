import hashlib, json, time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block("Genesis Block", "0")

    def create_block(self, data, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
            'data': data,
            'previous_hash': previous_hash,
            'hash': self.hash_block(data, previous_hash)
        }
        self.chain.append(block)
        return block

    def hash_block(self, data, previous_hash):
        block_string = json.dumps(str(data) + previous_hash, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def get_last_block(self):
        return self.chain[-1]

    def print_chain(self):
        for block in self.chain:
            print(json.dumps(block, indent=4))
