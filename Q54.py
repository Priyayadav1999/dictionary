a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 
4: ['Lynne Foster'], 5: ['Zachary Simon']}
dict={}
for i,j in a.items():
    for x in j:
        dict[i]=x
print(dict)