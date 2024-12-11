class Personne:
    def __init__(self,nom,prenom,age):
        self.nom=nom
        self.prenom=prenom
        self.age=age
    def sePresenter(self):
        print('Bonjour je suis {} {} et j ai {} ans'.format(self.nom,self.prenom,self.age))
class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule):
        super().__init__(nom,prenom,age)
        self.matricule=matricule
    def etudier(self):
        print('{} Etudie au moment {}'.format(self.prenom,self.matricule))
p=Etudiant('Baadi','Anass',21,'OWASP')
p.etudier()