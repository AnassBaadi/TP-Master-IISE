from abc import ABC,abstractmethod
class Vehicule(ABC):
    @abstractmethod
    def deplacer(self):
        pass
class Voiture(Vehicule):
    def deplacer(self):
        print('Deplacement sur la route national')

class Bicyclette(Vehicule):
    def deplacer(self):
        print('Deplacement sur la rue')
if __name__ == '__main__':
    # Instanciation des sous-classes
    voiture = Voiture()
    bicyclette = Bicyclette()

    # Appel de la méthode deplacer pour chaque véhicule
    voiture.deplacer()
    bicyclette.deplacer()