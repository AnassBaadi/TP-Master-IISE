class Rectangle:
    def __init__(self,largeur,hauteur):
        self.largeur=largeur
        self.hauteur=hauteur
    def calculer_surface(self):
        return self.largeur*self.hauteur
    def calculer_perimetre(self):
        return 2*(self.largeur+self.hauteur)
a=Rectangle(2,4)
print(a.calculer_surface())
print(a.calculer_perimetre())