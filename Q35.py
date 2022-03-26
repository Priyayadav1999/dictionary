from typing import List


dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}


sum=0
for x in dict.values():
    if type(x)==list:
        sum=sum+len(x)
print(sum)