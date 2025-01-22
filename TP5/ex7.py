import os
import shutil

#Copier "journal.txt" en "journal_copie.txt"
shutil.copy("journal.txt", "journal_copie.txt")
print("Fichier copié : 'journal_copie.txt' créé avec succès.")

# Étape 3 : Créer un dossier nommé "archives" (s'il n'existe pas déjà)
if not os.path.exists("archives"):
    os.makedirs("archives")
    print("Dossier 'archives' créé avec succès.")

# Déplacer "journal_copie.txt" dans le dossier "archives"
shutil.move("journal_copie.txt", "archives/")
print("Fichier 'journal_copie.txt' déplacé dans le dossier 'archives'.")
