dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
c=0
print("keys", "Values", "Count", end=" ")
print()
for x,y in dict_num.items():
    c+=1
    print(x, "   " ,y, "    " ,c, end=" ")
    print()