my_dict = {'a':50,'b':58,'c': 56,'d':40,'e':100,'f':20}
max=0
max1=" "
s_max=0
s_max1=" "
third_max=0
third_max1=" "
for j in my_dict:
    if my_dict[j]>max:
        third_max=s_max
        third_max1=s_max1
        s_max=max
        s_max1=max1
        max=my_dict[j]
        max1=j
    elif my_dict[j]!=max and my_dict[j]>s_max:
        third_max=s_max
        third_max1=s_max1
        s_max=my_dict[j]
        s_max1=j
    elif my_dict[j]!=max and my_dict[j]!=s_max and my_dict[j]>third_max:
        third_max=my_dict[j]
        third_max1=j
print(max1,s_max1,third_max1)