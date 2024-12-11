class Chien:
    def __init__(self,nom,race,age):
        self.nom=nom
        self.race=race
        self.age=age
    def aboyer(self):
        print('WOOF')
Max=Chien('Max','German Shepherd',2)
Max.aboyer()