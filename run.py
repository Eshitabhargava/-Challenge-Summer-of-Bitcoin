from utils.general_utils import *
from utils.transaction_utils import *
from models.transaction_model import Transaction


valid_transactions = {}

records = open("mempool.csv")
records.readline()
for record in records:
    record = record.strip().split(',')
    transaction = Transaction(record)
    if validate_transaction(valid_transactions, transaction.parents):
        valid_transactions[transaction.tx_id] = transaction

transactions_order = [list(valid_transactions.keys())][0]
sorted_transactions = sort_transactions(valid_transactions)

transactions = generate_block(sorted_transactions)
transactions = relativeSortArray(transactions, transactions_order)
generate_block_file(transactions)