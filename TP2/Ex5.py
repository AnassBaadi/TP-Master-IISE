class Animal:
    def faire_du_bruit(self):
        pass
class Chien(Animal):
    def faire_du_bruit(self):
        return 'Woof'

class Chat(Animal):
    def faire_du_bruit(self):
        return 'Miaw'

print('Le chien fait :',Chien().faire_du_bruit())
print('Le chat fait :',Chat().faire_du_bruit())
