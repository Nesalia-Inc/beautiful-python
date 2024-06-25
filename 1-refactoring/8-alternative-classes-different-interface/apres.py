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
        return "Woof!"
    
    def se_deplacer(self):
        return "Courir"


class Chat(Animal):
    
    def bruit(self):
        return "Miaou!"
    
    def se_deplacer(self):
        return "Marcher"




def faire_du_bruit(animal: Animal):
    print(animal.bruit())

def faire_se_deplacer(animal: Animal):
    print(animal.se_deplacer())


if __name__ == '__main__':
    chien = Chien("Médor", 12, 15.3)
    chat = Chat("Garfield", 4, 2.3)
    
    faire_du_bruit(chien)
    faire_du_bruit(chat)
    
    faire_se_deplacer(chien)
    faire_se_deplacer(chat)
    