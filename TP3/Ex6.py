from Ex4 import Produit

class Commande(Produit):
    """def __init__(self,nom,prix,mont,qte):
        super().__init__(nom,prix,mont)
        self.qte=qte"""
    def __init__(self,prod,qte):
        if isinstance(prod,Produit):
            self.prod=prod
        else:
            print('L objet passe comme argument doit etre instance de Produit')
        self.qte=qte
class Panier(Commande):
    def __init__(self,liste_com=None):
        self.liste_com=liste_com if liste_com and isinstance(liste_com[0],Commande) else []
    def ajouter_com(self,com):
        if com not in self.liste_com and isinstance(com,Commande):
            self.liste_com.append(com)
    def calc_total(self):
        s=0
        for com in self.liste_com:
            s+=com.prod.getPrix()*com.qte
        print('Le total du Panier :',s)

if __name__ == '__main__':
    # Création de quelques produits
    produit1 = Produit("Pomme", 1.2, 0)
    produit2 = Produit("Banane", 0.8, 0)
    produit3 = Produit("Orange", 1.5, 0)

    # Création de commandes pour ces produits
    commande1 = Commande(produit1, 10)  # 10 pommes
    commande2 = Commande(produit2, 5)   # 5 bananes
    commande3 = Commande(produit3, 8)   # 8 oranges

    # Création d'un panier
    panier = Panier()

    # Ajout des commandes au panier
    panier.ajouter_com(commande1)
    panier.ajouter_com(commande2)
    panier.ajouter_com(commande3)

    # Calcul et affichage du total
    panier.calc_total()