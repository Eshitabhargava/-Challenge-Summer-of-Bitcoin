"""
    Utility functions for Transaction objects
"""

def validate_transaction(previous_transactions, parent_transactions):
    """
        Checks if a Transaction is valid, 
        if all it's parent transactions occur before itself
    """
    if parent_transactions == ['']:
        return True
    for parent_transaction in parent_transactions:
        if parent_transaction not in previous_transactions:
            return False
    return True

def sort_transactions(transactions):
    """
        Sorts the list of Transaction Objects in 
        Descending order of Transaction Fee and
        Ascending order of Transaction weight
    """
    class reversor:
        def __init__(self, obj):
            self.obj = obj

        def __eq__(self, other):
            return other.obj == self.obj

        def __lt__(self, other):
            return other.obj < self.obj
    
    transactions = sorted(transactions.items(), key=lambda item: (item[1].fee, reversor(item[1].weight)), reverse=True )
    return transactions

def generate_block(sorted_transactions):
    """
        Selects Transactions from list 
        until combined weight crosses the Threshold
    """
    transactions = []
    weight = 0
    target = 4000000
    for transaction in sorted_transactions:
        if weight + transaction[1].weight <= target:
            weight += transaction[1].weight
            transactions.append(transaction[0])
            [transactions.append(x) for x in transaction[1].parents if x and x not in transactions]
    return transactions
  