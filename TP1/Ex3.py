def intersection(A,B):
    C=set()
    #depuis le cours autre methode C= A & B
    for i in A:
        for j in B:
            if i ==j:
                C.add(i)
    return C
#on peut ajouter ici un input de l'utilisateur
print(intersection({2,4,5,6},{4,5,7,8}))