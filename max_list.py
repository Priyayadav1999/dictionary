a=[[2,3,4],[7,3,9],[3,2,7]]
i=0
m=0
b=0
while i<len(a):
    sum=0
    j=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j+=1
    if m<sum:
        m=sum
        b=a[i]
    i+=1
print(m,b)
