d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
dict={}
for i in d1:
    if i in d2:
        dict.update({i:d1[i]+d2[i]})
    elif i not in d2:
        dict.update({i:d1[i]})
        # dict.update({i:d2[i]})
    for j in d2:
        if j not in d1:
            dict.update({j:d2[j]})
    
print(dict)
        

#  2nd method

#    wrong hai

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# dict={}
# for i in d1:
#     for j in d2: 
#         if i==j:
#             if i not in dict:
#                 dict[i]=d1[i]+d2[j]
#         else:
#             dict={**d1,**d2}
# print(dict)