l1=[(),(),('a','b'),('a','b','c'),'d']

for i in l1:
    if not i:
     l1.remove(i)
    

print(l1)