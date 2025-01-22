import csv

# Données d'exemple
contacts = [
    ["Nom", "Age", "Ville"],
    ["Anass", "21", "Rabat"],
    ["Abdenasser", "42", "Oujda"],
    ["Said", "16", "Tetouan"]
]
# Écriture des données dans le fichier CSV
with open("contacts.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(contacts)

print(f"Le fichier contacts.csv a été créé avec succès !")