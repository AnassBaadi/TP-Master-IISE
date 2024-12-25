class Vehicule:
    def __init__(self,marque,modele,annee):
        self.marque=marque
        self.modele=modele
        self.annee=annee
    def afficher_info(self):
        print('Vehicule ', self.marque,' ',self.modele,' ', self.annee)

class Moteur:
    def __init__(self,puissance,type):
        self.puissance=puissance
        self.type=type
    def afficher_moteur(self):
        print('Moteur de type {} et une puissance de {} cheval(aux)'.format(self.type,self.puissance))

class Voiture(Vehicule,Moteur):
    def __init__(self,vehicule,moteur,nb_places):
        self.vehicule=vehicule
        self.moteur=moteur
        self.nb_places=nb_places
        
    def afficher_info(self):
        print('Voiture ')
        print('Marque: {} || Modele:{} || Annee:{}'.format(self.vehicule.marque,self.vehicule.modele,self.vehicule.annee))
        print('Moteur de type {} et une puissance de {} cheval(aux)'.format(self.moteur.type,self.moteur.puissance))
        print("Nombre de places : ",self.nb_places)

class Moto(Vehicule,Moteur):
    def __init__(self,vehicule,moteur,type_moto):
        self.vehicule=vehicule
        self.moteur=moteur
        self.type_moto=type_moto
        
    def afficher_info(self):
        print('Moto ',self.type_moto)
        print('Marque: {} || Modele:{} || Annee:{}'.format(self.vehicule.marque,self.vehicule.modele,self.vehicule.annee))
        print('Moteur de type {} et une puissance de {} cheval(aux)'.format(self.moteur.type,self.moteur.puissance))

if __name__ == '__main__':
    # Création d'une instance de Vehicule pour la voiture
    vehicule_voiture = Vehicule("Toyota", "Corolla", 2020)
    moteur_voiture = Moteur(120, "Essence")
    voiture = Voiture(vehicule_voiture, moteur_voiture, 5)

    # Création d'une instance de Vehicule pour la moto
    vehicule_moto = Vehicule("Yamaha", "MT-07", 2022)
    moteur_moto = Moteur(75, "Essence")
    moto = Moto(vehicule_moto, moteur_moto, "Sportive")

    # Afficher les informations de la voiture
    print("Informations de la voiture :")
    voiture.afficher_info()

    # Afficher les informations de la moto
    print("Informations de la moto :")
    moto.afficher_info()
