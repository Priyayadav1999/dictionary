a={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
value=[]
key=[]
for i in a:
    key.append(i)
    value.append(a[i])
# print(value,key)

list=[]
for i in range(0,4):
    dict={}
    for j in range(len(key)):
        dict[key[j]]=value[j][i]
        
    list.append(dict)

print(list)


