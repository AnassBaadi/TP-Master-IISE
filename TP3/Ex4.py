class Produit:
    def __init__(self,nom,prix,mont):
        self.__nom=nom
        self.__prix=prix
        self.__mont=mont

    def getNom(self):
        return self.__nom
    def setNom(self,nom):
        self.__nom=nom
    def getPrix(self):
        return self.__prix
    def setPrix(self,prix):
        self.__prix=prix
    def getMont(self):
        return self.__mont
    def setMont(self,mont):
        self.__mont=mont

    def remise(self,rem): #rem signifie pourcentage de solde retiree du prix si rem=80% =>prix egal a 20% du prix original 
        if self.__prix >=self.__mont:
            if rem>0 and rem<100:
                self.__prix*=(100-rem)/100
            else:
                print('Taux de remise saisie doit etre compris entre 0 et 100')
if __name__=='__main__':
    p=Produit('Adidas Shoes',440,200)
    print(p.getPrix())
    p.remise(80) 
    print(p.getPrix())