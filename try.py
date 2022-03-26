# a='w3resource'
# dict={}
# for i in a:
#     c=0
#     for j in a:
#         if j==i:
#             c+=1
#     dict.update({i:c})
# print(dict)

# for loop
#list of  key & value = 

# a="megha kashyap"
# d={}
# c=0
# count=0
# for i in a:
#     if i==" ":
#         count+=1
#         d.update({"space"+str(count):" "})
#     else:
#         d.update({c:i})
#         c+=1
# print(d)

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
dict={}
for i in d1:
    for j in d2: 
        if i==j:
            if i not in dict:
                dict[i]=d1[i]+d2[j]
    dict={**d1,**d2}
print(dict)


