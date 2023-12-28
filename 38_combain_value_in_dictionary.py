from collections import Counter

dict = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

d1=Counter()

for i in dict:
        d1[i['item']] += i['amount']
print(d1)
