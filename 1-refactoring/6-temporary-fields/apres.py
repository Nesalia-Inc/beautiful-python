import random
from dataclasses import dataclass
from enum import Enum, auto


@dataclass
class Coordonnees:
    x : int 
    y : int
    


class Direction(Enum):
    HAUT = auto()
    BAS = auto()
    GAUCHE = auto()
    DROITE = auto()

    
class Joueur:
    def __init__(self) -> None:
        self.position = Coordonnees(0, 0)
        
        
    def deplacer(self, direction) -> None:    
        match direction:
            case Direction.HAUT: 
                self.position.y += 1
            case Direction.BAS: 
                self.position.y -= 1
            case Direction.GAUCHE: 
                self.position.x -= 1
            case Direction.DROITE: 
                self.position.x += 1
                
                
    def attaquer(self) -> str:
        return "Le joueur attaque !"
        
        
class Monstre:
    def __init__(self) -> None:
        self.position = Coordonnees(0, 0)
        
        
    def deplacer(self) -> None:    
        self.position.x += random.choice([-1, 1])
        self.position.y += random.choice([-1, 1])
                
                
    def attaquer(self) -> str:
        return "Le monstre attaque !"
        
        
        
if __name__ == '__main__':
    joueur = Joueur()
    monstre = Monstre()

    joueur.deplacer("haut")
    monstre.deplacer()

    print(joueur.position)  
    print(monstre.position)  

    print(joueur.attaquer())  # "Le joueur attaque!"
    print(monstre.attaquer())  # "Le monstre attaque!"
