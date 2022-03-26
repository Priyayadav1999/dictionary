list=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},
{"six":"9"},{"seven":"7"}]
# print(type(list))
a=[]
for i in list:
    for j in i.values():
        if j not in a:
            a.append(j)
print(a)


a=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, 
{"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
list=[]
for i in a:
    for j in i.values():
        if j not in list:
            list.append(j)
print(list)

