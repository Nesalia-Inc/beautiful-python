from typing import NamedTuple

from dataclasses import dataclass


class Adresse(NamedTuple):
    numero : int 
    rue : str 
    code_postal : int


@dataclass
class Personne:
    adresse : Adresse
    
    _nom : str 
    _telephone : str 
    
    
    @property
    def nom(self) -> str:
        return self._nom 
    
    @nom.setter
    def nom(self, nouveau_nom : str) -> None:
        if not nouveau_nom.isalpha():
            raise ValueError
        
        self._nom = nouveau_nom
        
    
    @property
    def telephone(self) -> str:
        return self._telephone
    
    @telephone.setter
    def telephone(self, nouveau_telephone : str) -> None:
        if len(nouveau_telephone) != 10:
            raise ValueError
        
        self._telephone = nouveau_telephone 
        
        
    @classmethod
    def create(cls, nom : str, telephone : str, adresse : Adresse) -> "Personne":
        if not nom.isalpha() or len(telephone) != 10:
            raise ValueError
        
        return cls(adresse, nom, telephone)
        
        
    
@dataclass    
class Compte:
    _email : str 
    _mdp : str 
        
    
    @property
    def email(self) -> str:
        return self._email 
    
    @property
    def mdp(self) -> str:
        return self._mdp
    
    @mdp.setter
    def mdp(self, nouveaux_mdp : str) -> None:
        if len(nouveaux_mdp) < 8:
            raise ValueError
        
        self._mdp = nouveaux_mdp
        
        
    @classmethod
    def create(cls, email : str, mdp : str) -> "Compte":
        if len(mdp) < 8:
            raise ValueError("Le mot de passe doit avoir au moins 8 caractères")
        
        return cls(email, mdp)
    
    
    
@dataclass
class Utilisateur:
    personne : Personne 
    compte : Compte 
    
    


if __name__ == '__main__':
    
    jean = Personne.create("Jean", "0701020304", Adresse(18, "Rue du Roi", 75000))
    compte = Compte.create("jean@gmail.com", "123456789")
    utilisateur = Utilisateur(jean, compte)
    
    print(utilisateur)