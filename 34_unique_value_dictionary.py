dict={"kiran":100,"himanshi":200,"yatin":300,"surbhi":200,"mansi":300,"hemal":200}
unique_dic=[]

for i in dict:
    if i not in unique_dic:
     unique_dic.append(i)
    
print("unique dic",unique_dic)


