d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {"a": 200, "b": 23, "e": 233}
for i in d2:
    if i in d1:
        d1[i]=d1[i]+d2[i]
    else:
        d1[i]=d2[i]

for j in d3:
    if j in d1:
        d1[j]=d1[j]+d3[j]
    else:
        d1[j]=d3[j]
print(d1)