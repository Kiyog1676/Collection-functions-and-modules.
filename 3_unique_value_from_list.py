l1=[20,45,6,90,78,5,45,70,20,56,90]

unique_list=[]

for i in l1:
    if i not in unique_list:
        unique_list.append(i)
print("unique list :",unique_list)