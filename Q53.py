a=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], 
[4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
c=0
dict={}
for i in a:
    j=1
    list=[]
    while j<len(i):
        list.append(i[j])
        j+=1
    c+=1
    dict[c]=list
print(dict)


# {1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'],
#  4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}