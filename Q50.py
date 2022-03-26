a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
new_list=[]
for i,j in a.items():
    new_list.append([i,j])
print(new_list)


#  2nd question

a={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
new_list=[]
for i,j in a.items():
    list=[]
    list.append(i)
    list.append(j)
    new_list.append(list)
print(new_list)