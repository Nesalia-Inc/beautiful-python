from typing import Protocol



class Monstre:
    def __init__(self, vie : int, attaque : int) -> None:
        self.__vie = vie 
        self.__attaque = attaque 
        
        
    @property
    def vie(self) -> int:
        return self.__vie
    
    @vie.setter
    def vie(self, nouvelle_vie : int) -> None:
        if nouvelle_vie <= 0:
            self.__vie = 0 
        elif nouvelle_vie >= 100:
            self.__vie = 100
        else:
            self.__vie = nouvelle_vie
    
    
    @property
    def attaque(self) -> int:
        return self.__attaque

    @attaque.setter
    def attaque(self, nouvelle_attaque : int) -> None:
        if nouvelle_attaque <= 0:
            raise ValueError("L'attaque ne peut pas être nulle")

        self.__attaque = nouvelle_attaque




class ImmutableMonstre(Protocol):
    @property
    def vie(self) -> int: ...
    @property
    def attaque(self) -> int: ... 
    
    
    
def afficher(monstre : ImmutableMonstre) -> None:
    print(f"Le monstre a actuellement {monstre.vie} de vie et {monstre.attaque} d'attaque.")




if __name__ == '__main__':
    afficher(Monstre(100, 10))