class CompteBancaire :
    def __init__(self,solde,titulaire):
        self.solde=solde
        self.titulaire=titulaire
    def deposer(self,montant):
        self.solde+=montant
    def retirer(montant):
        self.solde-=montant
    def afficher(self):
        print('Le solde Actuel dans votre Compte {} est :{}'.format(self.titulaire, self.solde))
d=CompteBancaire(2000,'Savings')
d.afficher()