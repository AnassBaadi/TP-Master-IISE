class Personne:
    def __init__(self,nom,prenom,age,amis=None):
        self.nom=nom
        self.prenom=prenom
        self.age=age
        if amis==None:
            amis=[]
        self.amis=amis
    def sePresenter(self):
        print('Bonjour je suis {} {} et j ai {} ans'.format(self.nom,self.prenom,self.age))

    def ajouter_ami(self,ami):
        self.amis.append(ami)
    
    def afficher_amis(self):
        for ami in self.amis:
            print(ami)
        print('*****************')

personne1 = Personne("El Idrissi", "Mohamed", 25)
personne2 = Personne("Bennani", "Fatima", 22)
personne3 = Personne("Alami", "Youssef", 30)

personne1.sePresenter()
personne2.sePresenter()
personne3.sePresenter()

personne1.ajouter_ami("Fatima Bennani")
personne1.ajouter_ami("Youssef Alami")

personne2.ajouter_ami("Mohamed El Idrissi")

print("Liste des amis de Mohamed El Idrissi :")
personne1.afficher_amis()

print("Liste des amis de Fatima Bennani :")
personne2.afficher_amis()