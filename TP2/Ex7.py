class Livre :
    def __init__(self,titre,auteur,annee_pub):
        self.titre=titre
        self.auteur=auteur
        self.annee_pub=annee_pub

class Biblio:
    def __init__(self, livres=None):
        if livres is None:
            livres = []
        self.livres = livres

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def afficher_livres(self):
        if not self.livres:
            print("La bibliothèque est vide.")
        else:
            for i, l in enumerate(self.livres, start=1):
                print(f"Livre {i} : {l.titre}")

if __name__ == "__main__":
    livre1 = Livre("1984", "George Orwell", 1949)
    livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
    livre3 = Livre("Harry Potter à l'école des sorciers", "J.K. Rowling", 1997)

    ma_biblio = Biblio()

    ma_biblio.ajouter_livre(livre1)
    ma_biblio.ajouter_livre(livre2)
    ma_biblio.ajouter_livre(livre3)

    print("Liste des livres dans la bibliothèque :")
    ma_biblio.afficher_livres()