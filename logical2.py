a=[{"name":"priya","age":22},{"name":"deepa","age":21},{"name":"shireen","age":20},
{"name":"kamini","age":19},{"name":"anjali","age":23}]

new_age=int(input("enter age="))
print("new_age is =",new_age)
for i in range(len(a)):
    for j in a[i]:
        if j=="age":
            if a[i][j]==new_age:
                print("equal to new_age",new_age)
            elif a[i][j]>new_age:
                print("greater to new_age",a[i][j])
            else:
                print("less than to new_age",a[i][j])

