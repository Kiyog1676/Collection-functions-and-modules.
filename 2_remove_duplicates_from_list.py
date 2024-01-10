l1=[20,40,60,45,20,9,60,2,9]


duplicates_list=[]

for i in l1:
    if i not in duplicates_list:
        duplicates_list.append(i)

print("duplicates list :",duplicates_list)




