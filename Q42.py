# d={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}

# user=int(input("enter any number="))
# c=0

# for i in d.values():
#     if i==user:
#         c+=1
# if c==len(d):
#     print(len(d))
#     print("true")
# else:
#     print("false")


# 2nd method

d={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
list=[]
for i in d.values():
    list.append(i)

i=0
c=0
a=list[i]
while i<len(list):
    if a==list[i]:
        c+=1
    i+=1
if c==len(list):
    print("True")
else:
    print("false")

