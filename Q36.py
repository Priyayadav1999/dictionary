a={'key1': 1, 'key2': 3, 'key3': 2}
b= {'key1': 1, 'key2': 2}

for x,y in a.items():
    if x in b.keys() and y in b.values():
        print(x,":",y," both x and y are presented in both dictionary")