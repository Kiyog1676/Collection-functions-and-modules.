l1=[]

num=int(input("enter your num :"))

for i in range (1,7):
    num=int(input("enter a number"))
    l1.append(num)
    total=sum(l1)
    

print("smallest num is ",min (l1))
print("largest num is ",max(l1))
print("total sum is :",total)