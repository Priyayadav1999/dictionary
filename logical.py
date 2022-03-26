# # # # a="priya"
# # # # dic={}
# # # # for i in range(len(a)):
# # # #     dic[a[i]]=a
# # # # print(dic)



# # a=[1,2,3,4]
# # b=[2,22,32,52]
# # dict={}
# # for i in a:
# #     for j in b :
# #         dict[i]=j
# #         b.remove(j)
# #         break
# # print(dict)

# # # a=[1,2]
# # # print(id(a))
# # # print(id([1,2]))
# # # x={"a":10,'b':0.5,'c':25,'d':2}
# # # min=x["a"]
# # # for i in x:
# # #     if x[i]<min:
# # #         min=x[i]
# # # print(min)

# # # a=[1,2,3,4]
# # # b=[2,22,42,32]
# # # d={}
# # # for key in a:
# # #     for value in b:
# # #         d[key]=value
# # #         b.remove(value)
# # #         break
# # # print(d)

# # a="roshni"
# # dict={}
# # c=0
# # for i in a:
# #     dict[c]=a
# #     c=c+1
# # print(dict,c)
a=[2,'a',4.5,'t',9.5,4.6,'b']
c=1
dict={}
for i in a:
    if type(i)==float:
        dict[c]=i
        # dict.update({c:i})
        c=c+1
print(dict)