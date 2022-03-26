a={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
dict={}

for i in a.keys():
    if a[i]>170:
        dict[i]=a[i]

print(dict)