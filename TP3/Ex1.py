from math import pi
from abc import ABC,abstractmethod
class Forme(ABC):
    @abstractmethod
    def calculer_surface(self):
        pass
class Cercle(Forme):
    def __init__(self,r):
        self.r=r
    def calculer_surface(self):
        return (self.r)**2*pi
class Rectangle(Forme):
    def __init__(self,longueur,largeur):
        self.longueur=longueur
        self.largeur=largeur
    def calculer_surface(self):
        return self.longueur*self.largeur
if __name__=='__main__':
    c=Cercle(4)
    r=Rectangle(8,3)
    print('La surface du cercle est :',c.calculer_surface())
    print('La surface du rectangle est :',r.calculer_surface())