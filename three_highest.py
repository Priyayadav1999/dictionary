my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
a=[]
max=0
s_max=0
third_max=0
for i in my_dict.values():
        if max<i:
            third_max=s_max
            s_max=max
            max=i
        elif i!=max and i>s_max:
            third_max=s_max
            s_max=i
        elif i!=max and i!=s_max and i>third_max:
            third_max=i
a.append(max)
a.append(s_max)
a.append(third_max)
print("three highest values are=",a)