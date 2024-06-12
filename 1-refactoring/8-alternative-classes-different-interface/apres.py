from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nom : str, age : int, poids : float) -> None:
        self.nom = nom 
        self.age = age 
        self.poids = poids
    
    
    @abstractmethod
    def bruit(self):
        pass
    
    @abstractmethod
    def se_deplacer(self):
        pass


class Chien(Animal):
    
    def bruit(self):
        return "Aboyer"
    
    def se_deplacer(self):
        return "Courir"


class Chat(Animal):
    
    def bruit(self):
        return "Miauler"
    
    def se_deplacer(self):
        return "Marcher"




def faire_du_bruit(animal: Animal):
    print(animal.bruit())

def faire_se_deplacer(animal: Animal):
    print(animal.se_deplacer())


