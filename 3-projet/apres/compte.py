import random

from dataclasses import dataclass, field

from client import Client


def generate_random_code() -> str:
    """Génère un code aléatoire pour un compte bancaire"""
    CODE_SIZE = 4
    
    def generate_random_digit() -> str:
        """Renvoie une valeur aléaoire entre 0 et 9"""
        return str(random.randint(0, 9))
    
    return ''.join([generate_random_digit() for _ in range(CODE_SIZE)])



class NotEnoughMoneyError(ValueError):
    pass 


@dataclass
class DonneesBancaires:
    _decouvert : float 
    
    _code : str = field(default_factory=generate_random_code)
    _argent : float = 0
    
    
    @property
    def decouvert(self) -> float:
        return self._decouvert
    
    @decouvert.setter
    def decouvert(self, nouveau_decouvert : float) -> None:
        self._decouvert = nouveau_decouvert
    
    
    @property
    def code(self) -> str:
        return self._code
    
    def generate_new_code(self) -> None:
        self._code = generate_random_code()
        
        
    @property
    def argent(self) -> float:
        return self._argent
    
    @argent.setter
    def argent(self, nouvel_argent : float) -> None:
        if nouvel_argent < self._decouvert:
            raise NotEnoughMoneyError(f"Le découvert est limité à {self._decouvert} et vous avez voulu retirer {nouvel_argent}.")
        
        self._argent = nouvel_argent
    




class Compte:
    def __init__(self, client : Client, donnees : DonneesBancaires):
        self._client = client 
        self._donnees = donnees
        
        
    @property
    def client(self) -> Client:
        return self._client 
    
    
    @property
    def decouvert(self) -> float:
        return self._donnees.decouvert 
    
    @decouvert.setter
    def decouvert(self, nouveau_decouvert : float) -> None:
        self._donnees.decouvert = nouveau_decouvert
    
    @property
    def code(self) -> str:
        return self._donnees.code
    
    def generate_new_code(self) -> None:
        self._donnees.generate_new_code()
    
    
    @property
    def argent(self) -> float:
        return self._donnees.argent
    
    @argent.setter
    def argent(self, nouvel_argent : float) -> None:
        self._donnees.argent = nouvel_argent
    
    
        
        
    @classmethod
    def create(cls, client : Client, decouvert : float) -> "Compte":
        donnees = DonneesBancaires(decouvert)
        return cls(client, donnees)
    
    
    
if __name__ == '__main__':
    d = DonneesBancaires(-100)
    
    d.argent = 250
    d.argent -= 500