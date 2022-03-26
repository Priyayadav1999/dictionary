a={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
dict={}
for i,y in a.items():
    y.clear()
    dict[i]=y
print(dict)