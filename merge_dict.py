
# Merge Dictionaries using dict.update()
a={1:456,2:567}
b={4:"priya",3:"pooja"}

a.update(b )
print(a)

#  merge using unpacking operator
a={1:456,2:567}
b={4:"priya",3:"pooja"}

c={**a,**b}
print(c)


# Merge Dictionaries using for Loop 
a={1:456,2:567}
b={4:"priya",3:"pooja"}

for x,y in b.items():
    a[x]=y
print(a)

