from flask import Flask,jsonify,request
from blockchain import Blockchain
from uuid import uuid4

app = Flask(__name__)

node_identifier = str(uuid4()).replace('-','')
#instatiate Blockchain Class
bc = Blockchain()

@app.route('/mining',methods=['GET'])
def mine():
    last_block = bc.last_block
    last_proof = last_block['proof']
    proof = bc.proof_of_work(last_proof)

    bc.new_transaction(
        sender = "0",
        recipient=node_identifier,
        amount=1,
    )
    previous_hash = bc.hash(last_block)
    block = bc.new_block(proof,previous_hash)

    respone = {
        'hash':bc.hash(block),
        'message':"New Block Forged",
        'index':block['index'],
        'transactions':block['transactions'],
        'proof':block['proof'],
        'previous_hash':block['previous_hash']
    }
    return jsonify(respone),200


@app.route('/new/transaction',methods=['POST'])
def new_transaction():
    value = request.get_json()
    required = ['sender','recipient','amount']
    if not all(k in value for k in required):
        return 'Missing value',400
    index = bc.new_transaction(
        value['sender'],
        value['recipient'],
        value['amount']
    )
    response = {
        'message':"Transaction akan ditambahkan kedalam Block {}".format(index)
    }
    return jsonify(response),201


@app.route('/blockchain',methods=['GET'])
def blockchain_route():
    response = {
        'chain':bc.chain,
        'length':len(bc.chain)
    }
    return jsonify(response),200


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
