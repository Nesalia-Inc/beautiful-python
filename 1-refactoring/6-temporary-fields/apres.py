import random
from typing import Protocol
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


class Entite(Protocol):
    position : Coordonnees
    
    def deplacer(self) -> None: ...
    def attaquer(self) -> None: ...
    
    
    
class Joueur:
    def __init__(self) -> None:
        self.position = Coordonnees(0, 0)
        self.direction = Direction.HAUT
        
        
    def deplacer(self) -> None:    
        match self.direction:
            case Direction.HAUT: 
                self.position.y += 1
            case Direction.BAS: 
                self.position.y -= 1
            case Direction.GAUCHE: 
                self.position.x -= 1
            case Direction.DROITE: 
                self.position.x += 1
                
                
    def attaquer(self) -> None:
        print("Le joueur attaque !")
        
        
class Monstre:
    def __init__(self) -> None:
        self.position = Coordonnees(0, 0)
        
        
    def deplacer(self) -> None:    
        self.position.x += random.choice([-1, 1])
        self.position.y += random.choice([-1, 1])
                
                
    def attaquer(self) -> None:
        print("Le joueur attaque !")
        
        
        
def deplacer(entite : Entite) -> None:
    entite.deplacer()