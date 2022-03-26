a={"a":100,"b":200,"c":300}
b={"a":300,"b":200,"d":400}

for i in b:
    if i in a:
        a[i]=a[i]+b[i]
    else:
        a[i]=b[i]
print(a)
