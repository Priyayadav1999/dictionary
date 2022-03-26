a={'c1':[1,2,3],'c2':[5,6,7],'c3':[9,10,11]}
list=[]
for i,j in a.items():
    list.append(j)
    print(i,end=" ")
print()

x=0
while x<len(list):
    y=0
    while y<len(list):
        print(list[y][x],end=" ")
        y+=1
    print()
    x+=1