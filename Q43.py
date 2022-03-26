dict=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
dict1={}
for i in dict:
    list=[]
    for j in dict:
        if i[0]==j[0]:
            list.append(j[1])

    dict1[i[0]]=list
print(dict1)