# Sample data: 
dict= {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

key=[]
value=[]
max=0
max_item=" "
for i,j in dict.items():
    if max<j:
        max=j
        max_item=i
print(max_item," ", max)