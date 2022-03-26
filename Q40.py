a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]

dict={}

i=0
while i<len(a):
    dict[a[i]]={b[i]:c[i]}
    i+=1
print(dict)