a={'c1': 'Red', 'c2': 'Green', 'c3': None}
dict={}

for i in a.keys():
    if a[i] == False or a[i]== None:
        pass
    else:
        dict[i]=a[i]


print(dict)