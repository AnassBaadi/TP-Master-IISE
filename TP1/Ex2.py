def max_tuple(tuple):
    max=tuple[0]
    for e in tuple:
        if e > max :
            max=e
    return max
l=[]
for k in range(5):
    a=int(input('Saisir un entier {} :'.format(k+1)))
    l.append(a)
t=(l[0],l[1],l[2],l[3],l[4])
print(max_tuple(t))