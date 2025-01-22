import json

# Dictionnaire Python avec des informations sur des étudiants.
etudiants = [
    {"Nom": "Anass", "Âge": 21, "Note": 19},
    {"Nom": "Baadi", "Âge": 20, "Note": 18},
    {"Nom": "Anass Baadi", "Âge": 22, "Note": 20}
]

with open("etudiants.json", "w") as file:
    json.dump(etudiants, file)

# Lecture du fichier JSON
with open("etudiants.json", "r") as file:
    data = json.load(file)
    for etudiant in data:
        print(etudiant)