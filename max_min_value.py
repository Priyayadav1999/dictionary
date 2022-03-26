a={"x":23,"y":4,"p":4056,"q":567,"o":6}
max=0
for i in a:
    if max<a[i]:
        max=a[i]
print(max)

temp= min(a.values())
for key in a:
    if a[key]==temp:
        print(temp)
    

