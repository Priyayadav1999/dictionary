from typing import Counter


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
a=Counter(dic1)+Counter(dic2)+Counter(dic3)
print(a)

# 1st method

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dict={}
dict.update(dic1)
dict.update(dic2)
dict.update(dic3)
print(dict)

# 2nd  method