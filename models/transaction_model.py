"""
    Defines Transaction object 
"""

class Transaction:
    def __init__(self, record):
        self.tx_id = record[0]
        self.fee = int(record[1])
        self.weight = int(record[2])
        self.parents = record[3:][0].split(';')
