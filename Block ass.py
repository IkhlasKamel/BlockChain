# first:imports! We’ll need hashlib for the encryption, JSON to format our blocks, and time for each block’s timestamp.


# For timestamp
from inspect import BlockFinder
from time import time
# in order to add digital
import hashlib

# To store data
import json


# create a Blockchain class


class Blockchain(object):

    # This function is created
    # to create the very first
    # block and set its hash to "0"
    def __init__(self):
        # chain empty list that we’ll add blocks to. Quite literally our ‘block-chain’.
        self.chain = []
        # hen users send our coins to each other, their transactions will sit in this array
        self.pending_transactions = []
        # until we approve & add them to a new block

        self.new_block(     # we’ll use it to add each block to the chain
            previous_hash="The Times 03/jan/2009 Chancellor on  brink of second bailout for banks .", proof=100)
        # Satoshi’s message from the Bitcoin genesis block

        # Step 2: Write a Function to Build New Blocks

        def new_block(self, proof, previous_hash=None):
            block = {

                # index: Take the length of our blockchain and add 1 to it
                'index': len(self.chain) + 1,
                # using our time() import, stamp the block when it’s created.
                'timestamp': time(),
                # any transactions that are sitting in the ‘pending’ list will be included in our new block.
                'transactions': self.pending_transactions,
                'proof': proof,  # this comes from our miner who thinks they found a valid “nonce”, or “proof
                # a hashed version of the most recent approved block
                'previous_hash': previous_hash or (self.chain[-1]),

            }

        self.pending_transactions = []
        self.chain.append(BlockFinder)
        return BlockFinder


@property
# use to call our chain and receive the block that was added most recently
def last_block(self):

    return self.chain[-1]


def new_transaction(self, sender, recipient, amount):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount

    }

    # we use it when use the a new block is mined and added to our blockchain
    self.pending_transactions.append(transaction)
    return self.last_block['index']+1


def hash(self, block):  # hash an encryption hash function, which takes in some text string
    string_object = json.dumps(block, sort_key=True)
    block_string = string_object.encode | ()

    raw_hash = hashlib.sha256(block_string)

    hex_hash = raw_hash.hexdigest()
    return hex_hash


blockchain = blockchain()

t1 = Blockchain.__new__transaction("Satoshi", "Mike", '5 BTC')
t2 = Blockchain.__new__transaction("Mike", "Satoshi", '1 BTC')
t3 = Blockchain.__new__transaction("Satoshi", "Hal finney", '5 BTC')
Blockchain.new_block(12345)

t4 = Blockchain.__new__transaction("Mike", "Alice", '1 BTC')
t5 = Blockchain.__new__transaction("Alice", "Bob", '0.5 BTC')
t6 = Blockchain.__new__transaction("Bob", "Mike", '0.5 BTC')
Blockchain.new_block(6789)

print("Blockchain :", Blockchain.chain)
