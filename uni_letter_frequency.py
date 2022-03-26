######################### WHILE LOOP

# a="MISSISSIPPI"
# dic={}
# list=[]
# i=0
# while i<len(a):
#     j=0
#     c=0
#     while j<len(a):
#         if a[i]==a[j]:
#             c+=1
#         j+=1
#     if a[i] not in dic:
#         dic.update({a[i]:c})
#     i+=1
# print(dic)



############################## for loop

a="MISSISSIPPI"
dic={}
for i in a:
    c=0
    for j in a:
        if i==j:
            c+=1
    if i not in dic:
        dic.update({i:c})
print(dic)
