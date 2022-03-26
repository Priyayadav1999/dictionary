list=['a','b','a','b','c','d','a','e','d']
dict={}
i=0
while i<len(list):
    c=0
    j=0
    while j<len(list):
        if list[i]==list[j]:
            c+=1
        j+=1
    dict[list[i]]=c
    i+=1
print(dict)




