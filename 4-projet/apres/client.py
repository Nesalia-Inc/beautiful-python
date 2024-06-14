import random

from dataclasses import dataclass, field




def generer_identifiant() -> int:
    identifiant = random.randint(100_000, 1_000_000)
        
    return identifiant
        




@dataclass
class Adresse:
    numero : int 
    rue : str 
    code_postal : int 


@dataclass
class Personne:
    prenom : str 
    nom : str 
    telephone : str 



@dataclass
class Client:
    personne : Personne 
    adresse : Adresse
    
    identifiant : int = field(default_factory=generer_identifiant)
    
    
    @property
    def prenom(self) -> str:
        return self.personne.prenom
    
    @property
    def nom(self) -> str:
        return self.personne.nom
    
    @property
    def nom_complet(self) -> str:
        return self.prenom + " " + self.nom
    
    @property
    def telephone(self) -> str:
        return self.personne.telephone
    
    
    
    @classmethod
    def create(cls, personne : Personne, adresse : Adresse) -> "Client":
        return cls(personne, adresse)
    
    

