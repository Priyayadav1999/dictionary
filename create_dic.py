list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
i=0
dic={}
while i<len(list1):
    dic.update({list1[i]:list2[i]})
    i+=1
print(dic)