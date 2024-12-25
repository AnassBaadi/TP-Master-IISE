from Ex1 import *
def afficher_surface(F):
    k=1
    for e in F:
        print('La surface de la forme {} est : {}'.format(k,e.calculer_surface()))
        k+=1

r=Rectangle(2,4)
r1=Rectangle(8,5)
c=Cercle(7)
l=[r,r1,c]
afficher_surface(l)