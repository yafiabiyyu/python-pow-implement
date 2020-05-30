import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

        #create genesis block
        self.new_block(previos_hash=1,proof=100)
    
    def new_block(self,proof,previous_hash=None):
        block = {
            'index':len(self.chain) + 1,
            'timestamp':self.current_transaction,
            'proof':proof,
            'previous_hash':previous_hash or self.hash(self.chain[-1])
        }

        #rest the current list of transactions
        self.current_transaction = []
        self.chain.append(block)
        return block

    def new_transaction(self,sender,recipient,amount):
        self.current_transaction.append({
            'sender':sender,
            'recipient':recipient,
            'amount':amount
        })

        return self.last_block['index']+1

    @staticmethod
    def hash(block):
        pass

    @property
    def last_block(self):
        pass

