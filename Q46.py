a=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
list=[]
for i in a:
    dict={}
    for x,y in i.items():
        dict[x]=int(y)
    list.append(dict)

print(list)



# 2nd question

a=[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
list=[]
for i in a:
    dict={}
    for x,y in i.items():
        dict[x]=float(y)
    list.append(dict)

print(list)