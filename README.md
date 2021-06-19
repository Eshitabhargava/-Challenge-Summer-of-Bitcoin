# Challenge/Summer-of-Bitcoin

#####Tasks involved, as in the Solution Code:

1. Parse CSV 
2. While Parsing, keep checking if the transaction record at hand is a Valid one. 
   If the record does not have any Parent transactions -> add it into a dict of *valid_transactions*
   Else check for it's Parent transactions to be valid, by checking for their occurrence in the dict of *valid_transactions*
   NOTE: A dict with transaction id against transaction objects has been maintained, so as to undo the need of lookups to get data relevant OF the same transaction, such as it's      fee or weight.
3. Once we have a list of valid transactions at hand, we will sort this list on basis of two paramteres:
   3.1 Fee of Transactions should be in Descending order
   3.2 Weight of Transactions should be in Ascending order
4. Next up we will choose Transactions to generate a block, so as to maximise fee, given that the combined sum of all the chosen Transactions doesn't cross the Threshold value of    4,000,000
5. Since we need to write the Transactions in the order they occur, we go about sorting them in the said order.
6. Finally write the chosen Transactions into output file block.txt
