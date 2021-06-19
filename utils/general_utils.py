from typing import List

def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
        """
            Sorts elements of arr1 in the order of their occurrence in arr2
        """
        D = {v : i for i, v in enumerate(arr2)}
        def custom_sort(val):
            index = D.get(val, -1) 
            return (1, val) if index == -1 else (0, index)
        return sorted(arr1, key=custom_sort)

def generate_block_file(transactions):
    """
        writes transactions to output file block.txt
    """
    file = open("block.txt","a")
    for transaction in transactions:
        file.write(str(transaction) + '\n')
    file.close()
