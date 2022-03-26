d1=[{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]


sum=0
for i in d1:
    for j in i.values():

        if j==str(j):
            print(j)
            pass
        elif j==True or j==False:
            print(j)
            pass
        else:
            sum=sum+j
            print(j)
# print(sum)