class Employe:
    def __init__(self,nom,prenom,salaire):
        self.nom=nom
        self.prenom=prenom
        self.salaire=salaire
class Manager(Employe):
    def __init__(self,nom,prenom,salaire,liste_emp=None):
        super().__init__(nom,prenom,salaire)
        self.liste_emp=liste_emp if liste_emp else []
    def ajouter_emp(self,emp):
        if emp not in self.liste_emp:
            self.liste_emp.append(emp)
            print('Employe {} a ete ajoute'.format(emp.nom))
        else:
             print('Employe {} deja ajoute'.format(emp.nom))
    def afficher_emp(self):
        print('Liste des employes sous supervision du Manager ',self.nom,':')
        for emp in self.liste_emp:
            print('Nom: {} ||Prenom: {} ||Salaire:{}'.format(emp.nom,emp.prenom,emp.salaire))
if __name__ == "__main__":
    # Création d'employés
    emp1 = Employe("El Hajji", "Omar", 8000)
    emp2 = Employe("Bennani", "Fatima", 7500)
    emp3 = Employe("Lahlou", "Youssef", 6800)

    # Création d'un manager
    manager = Manager("Amrani", "Khadija", 15000)

    # Ajout d'employés au manager
    manager.ajouter_emp(emp1)
    manager.ajouter_emp(emp2)
    manager.ajouter_emp(emp3)

    # Affichage des employés supervisés
    manager.afficher_emp()