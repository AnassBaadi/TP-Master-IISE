# Partie de Saisie de lignes
with open("phrases.txt","w") as file:
    for k in range(3):
        line=input(f"Donner la ligne {k+1} :")
        file.write(line+"\n")