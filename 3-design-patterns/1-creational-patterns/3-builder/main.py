from dataclasses import dataclass
from enum import Enum, auto


class Pain(Enum):
    CLASSIQUE = auto()
    COMPLET = auto()
    
    
class Viande(Enum):
    BOEUF = auto()
    POULET = auto()
    DINDE = auto()
    
    
class Fromage(Enum):
    CLASSIQUE = auto()
    CHEVRE = auto()
    CAMEMBERT = auto()
    
    
class Sauce(Enum):
    KETCHUP = auto()
    MAYONNAISE = auto()
    BARBECUE = auto()
    



@dataclass
class Hamburger:
    pain : Pain 
    viande : Viande  
    fromage : Fromage 
    sauces : list[Sauce]
    
    
    
class HamburgerBuilder:
    def __init__(self) -> None:
        self.reinitialiser()
        
        
    def reinitialiser(self) -> "HamburgerBuilder":
        self.pain = Pain.CLASSIQUE
        self.viande = Viande.BOEUF
        self.fromage = Fromage.CLASSIQUE
        self.sauces : list[Sauce] = []
        
        return self
    
    
    def set_pain(self, pain : Pain) -> "HamburgerBuilder":
        self.pain = pain 
        return self
    
    def set_viande(self, viande : Viande) -> "HamburgerBuilder":
        self.viande = viande 
        return self
    
    def set_fromage(self, fromage : Fromage) -> "HamburgerBuilder":
        self.fromage = fromage 
        return self
    
    def add_sauce(self, sauce : Sauce) -> "HamburgerBuilder":
        self.sauces.append(sauce) 
        return self
    
    def build(self) -> Hamburger:
        return Hamburger(self.pain, self.viande, self.fromage, self.sauces)
    
    
    
if __name__ == '__main__':
    builder = HamburgerBuilder()
    
    hamburger = builder.set_pain(Pain.COMPLET) \
                       .set_fromage(Fromage.CHEVRE) \
                       .build()
    
    print(hamburger)