def compte_occurences(liste):
    dict={}
    for k in liste:
        nbr=0
        for m in liste:
            if k==m :
                nbr+=1
        dict[k]=nbr
    return dict
print(compte_occurences(['a','a','b','c','a']))