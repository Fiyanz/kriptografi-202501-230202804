import hashlib
import time
import json


class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

    def to_dict(self):
        return {
            'index': self.index,
            'previous_hash': self.previous_hash,
            'data': self.data,
            'timestamp': self.timestamp,
            'nonce': self.nonce,
            'hash': self.hash
        }

    @staticmethod
    def from_dict(block_dict):
        block = Block.__new__(Block)
        block.index = block_dict['index']
        block.previous_hash = block_dict['previous_hash']
        block.data = block_dict['data']
        block.timestamp = block_dict['timestamp']
        block.nonce = block_dict['nonce']
        block.hash = block_dict['hash']
        return block


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 6

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

    def save_to_file(self, filename="praktikum/week13-tinychain/logs/blockchain.json"):
        data = {
            'difficulty': self.difficulty,
            'chain': [block.to_dict() for block in self.chain]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Blockchain saved to {filename}")

    def load_from_file(self, filename="praktikum/week13-tinychain/logs/blockchain.json"):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.difficulty = data['difficulty']
            self.chain = [Block.from_dict(block_dict) for block_dict in data['chain']]
            print(f"Blockchain loaded from {filename}")
            return True
        except FileNotFoundError:
            print(f"File {filename} not found")
            return False
        except Exception as e:
            print(f"Error loading blockchain: {e}")
            return False



if __name__ == "__main__":
    my_chain = Blockchain()
    
    print("Mining block 1...")
    my_chain.add_block(Block(1, "", "Transaksi A -> B: 10 koin"))

    print("Mining block 2...")
    my_chain.add_block(Block(2, "", "Transaksi B -> C: 5 koin"))

    print("Mining block 3...")
    my_chain.add_block(Block(3, "", "Transaksi C -> A: 3 koin"))

    print("\nBlockchain Status:")
    print(f"Valid: {my_chain.is_chain_valid()}")
    
    print("\nBlockchain Contents:")
    for block in my_chain.chain:
        print(f"Block #{block.index}: {block.data}")
        print(f"  Hash: {block.hash}")
        print(f"  Previous: {block.previous_hash}")
        print(f"  Nonce: {block.nonce}\n")

    my_chain.save_to_file()

    print("\nTesting Load from File:")
    new_chain = Blockchain()
    if new_chain.load_from_file():
        print(f"Loaded {len(new_chain.chain)} blocks")
        print(f"Valid: {new_chain.is_chain_valid()}")