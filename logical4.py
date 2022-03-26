a={1:"one",2:"two",3:"three"}

# x=a.items()
# print(x)
b={6:"six"}

a.update({4:"four"})
a.update( b)
a[4]="five"
# a.popitem()
print(a)