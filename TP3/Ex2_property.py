class Personne():
    def __init__(self,nom,prenom,age):
        self.__nom=nom
        self.__prenom=prenom
        self.__age=age
    
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,nom):
        self.__nom=nom
    
    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self,prenom):
        self.__prenom=prenom
    
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age=age

"""
    def _getNom(self):
        return self.__nom
    def _setNom(self,nom):
        self.__nom=nom
    nom=property(_getNom,_setNom)

    def _getPrenom(self):
        return self.__prenom
    def _setPrenom(self,Prenom):
        self.__prenom=Prenom
    prenom=property(_getPrenom,_setPrenom)

    def _getAge(self):
        return self.__age
    def _setAge(self,age):
        self.__age=age
    age=property(_getAge,_setAge)
"""

p=Personne("Baadi","Anass",21)
print('Nom: {} || Prenom: {} || Age: {}'.format(p.nom,p.prenom,p.age))
p.age=22
print('Nom: {} || Prenom: {} || Age: {}'.format(p.nom,p.prenom,p.age))