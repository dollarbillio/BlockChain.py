blockchain = [-1]

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount):
    '''
    a chain of recursive blocks
    [1, [1, 2], [[1, 2] 3]]]
    '''
    blockchain.append([get_last_blockchain_value(), transaction_amount])


add_value(2)
add_value(0.9)
add_value(10)

print (blockchain)

# Lesson 25