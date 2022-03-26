dict = {
'Alex': ['subj1', 'subj2', 'subj3'],
'David': ['subj1', 'subj2']}
sum=0
for i in dict.values():
    sum=sum+len(i)
print(sum)