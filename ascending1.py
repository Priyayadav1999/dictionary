dict={'math':81,'physics':83,'chemistry':87}
key=[]
value=[]

for i,j in dict.items():
    key.append(i)
    value.append(j)

for x in range(len(key)):
    for y in range(len(key)):
        if value[y]<value[x]:
            temp=value[x]
            value[x]=value[y]
            value[y]=temp
            temp1=key[x]
            key[x]=key[y]
            key[y]=temp1
list=[]
for i in range(len(key)):
    list.append((key[i],value[i]))
print(list)



                  #  WITH METHODS #
# a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# a=sorted(a.keys())
# print(a)
# print(type(a))