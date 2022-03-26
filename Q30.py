a={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
dict={}
for x ,y in a.items():
    b=" "
    for j in x:
        if j==" " :
            pass
        else:
            b=b+j
    dict[b]=y
print(dict)