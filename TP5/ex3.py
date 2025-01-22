# Partie de Saisie de lignes
choix=input("Voulez vous ajouter d'autres phrases ? (o/n) :").lower()
if choix== 'o':
    n=int(input("Donner le nombre de lignes que vous voulez ajouter :"))
    with open("phrases.txt","a") as file:
        for k in range(n):
            line=input(f"Donner la ligne {k+1} :")
            file.write(line+"\n")
else:
    print("Aucune phrase n'a ete ajoutee !")