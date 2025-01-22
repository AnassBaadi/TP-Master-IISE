# Partie de Saisie de lignes
with open("exemple.txt","w") as file:
    for k in range(5):
        line=input(f"Donner la ligne {k+1} :")
        file.write(line+"\n")

# Partie d'affichage
with open("exemple.txt","r") as file:
    lignes=file.readlines()
    i=1
    for l in lignes :
        print(i,l.strip())
        i+=1