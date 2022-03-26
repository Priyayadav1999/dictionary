my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

for i,j in my_dict.items():
    print(i,end=" ")
    for x in j:
        print(x,end=" ")
    print()


