import os

# Renommer le fichier phrases.txt en anciennes_phrases.txt
os.rename("phrases.txt", "anciennes_phrases.txt")

# Supprimer le fichier
os.remove("anciennes_phrases.txt")