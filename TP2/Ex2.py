class Voiture:
    def __init__(self,marque,modele,annee) :
        self.marque=marque
        self.modele=modele
        self.annee=annee
    def afficher(self):
        return self.marque +' '+ self.modele+' '+ str(self.annee)
v1=Voiture('Mercedes','GLE','2018') 
v2=Voiture('Dodge','Challenger SRT','2022')
marque=input('Saisir la marque de la voiture :')
modele=input('Saisir le modele de la voiture :')
annee=int(input('Saisir l annee de la voiture :'))
v=Voiture(marque,modele,annee)
print(v1.afficher()) 
print(v2.afficher())
print(v.afficher())