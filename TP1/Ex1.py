def somme_liste(liste):
    s=0
    for e in liste:
        s+=e
    return s
l=[]
n=int(input('Combien de nombres dans la liste ? '))
for k in range(n):
    a=int(input('Saisir un entier {} :'.format(k+1)))
    l.append(a)
print('La somme est :',somme_liste(l))