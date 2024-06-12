class Chien:
    def __init__(self, nom : str, age : int, poids : float) -> None:
        self.nom = nom 
        self.age = age 
        self.poids = poids

    def aboyer(self):
        return "Aboyer"
    
    def courir(self):
        return "Courir"

class Chat:
    def __init__(self, nom : str, age : int, poids : float) -> None:
        self.nom = nom 
        self.age = age 
        self.poids = poids

    def miauler(self):
        return "Miauler"
    
    def marcher(self):
        return "Marcher"
