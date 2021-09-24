"""
Given a list of item transactions: [b,a,b,a,c,c,b]
  - sort the transactions in descending order by number of items sold
  - then alphabetically by item name 
  - save in the required format ['b 3', 'a 2', 'c 2']
"""

transactions = ['apricot','capsicum','capsicum','banana','banana','banana','banana','banana','capsicum','capsicum','apricot','apricot','apricot']

from collections import Counter
def get_transactions(transactions):
    count = dict(Counter(transactions))
    count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    mylist = []
    for i,j in count:
        string = i + ' ' + str(j)
        mylist.append(string)
    return mylist
  
 
get_transactions(transactions)

['banana 5', 'apricot 4', 'capsicum 4']
