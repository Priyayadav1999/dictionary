a={'w': 8, '3': 11, 'r': 5, 'e': 2, 's': 6, 'o': 1, 'u': 4, 'c': 1}
list=[]

for i in a.values():
    list.append(i)


for j in range(len(list)):
    for k in range(len(list)):
        if list[j]<list[k]:
            temp=list[j]
            list[j]=list[k]
            list[k]=temp

print("first maximum =",list[-1])
print("second maximun =",list[-2])
print("third maximum =",list[-3])
print("minimum num=",list[0])