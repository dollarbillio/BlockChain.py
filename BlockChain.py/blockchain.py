blockchain = [[-1]]

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount, last_transaction = blockchain[-1]):
    '''
    a chain of recursive blocks
    [1, [1, 2], [[1, 2] 3]]]
    '''
    blockchain.append([last_transaction, transaction_amount])

tx_amount = int (input ("Your Transaction Amount Please? "))
add_value(tx_amount)

tx_amount = int (input ("Your Transaction Amount Please? "))
add_value(last_transaction = get_last_blockchain_value(), transaction_amount=tx_amount)

tx_amount = int (input ("Your Transaction Amount Please? "))
add_value(tx_amount, get_last_blockchain_value())

print (blockchain)

