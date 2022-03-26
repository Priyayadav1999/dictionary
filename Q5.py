a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
key=[]
value=[]
for i in a:
    key.append(i)
    value.append(a[i])
# print(key)
# print(value)

for i in range(len(value)):
    for j in range(len(value)):
        if key[i]>key[j]:
            key[i],key[j]=key[j],key[i]
        if value[i]>value[j]:
            value[i],value[j]=value[j],value[i]

desc={}
for index in range(len(key)):
    desc[key[index]]=value[index]
print(desc)