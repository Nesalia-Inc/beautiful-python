class Chien:
    def __init__(self, nom : str, age : int, poids : float) -> None:
        self.nom = nom 
        self.age = age 
        self.poids = poids

    def aboyer(self):
        return "Woof!"
    
    def courir(self):
        return "Courir"


class Chat:
    def __init__(self, nom : str, age : int, poids : float) -> None:
        self.nom = nom 
        self.age = age 
        self.poids = poids

    def miauler(self):
        return "Miaou"
    
    def marcher(self):
        return "Marcher"



if __name__ == '__main__':
    chien = Chien("Médor", 12, 15.3)
    chat = Chat("Garfield", 4, 2.3)
    
    