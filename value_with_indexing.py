a="megha kashyap"
d={}
c=0
count=0
for i in a:
    if i==" ":
        count+=1
        d.update({"space"+str(count):" "})
    else:
        d.update({c:i})
        c+=1
print(d)
