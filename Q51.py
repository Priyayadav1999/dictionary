a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
dict={}
for i,j in a.items():
    list=[]
    for x in j:
        if x%2==0:
            list.append(x)

    dict[i]=list
print(dict)


#  2nd question


a={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
dict={}
for i,j in a.items():
    list=[]
    for x in j:
        if x%2==0:
            list.append(x)

    dict[i]=list
print(dict)
    
