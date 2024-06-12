


class Ville:
    def __init__(self, nom : str, code_postal : int, habitants : int) -> None:
        self._nom = nom 
        self._code_postal = code_postal
        self._habitants = habitants
        
        
    def __str__(self) -> str:
        return f"La ville de {self.nom} se situe dans le {self.code_postal} et possède {self.habitants} habitants"
    
    
    @property
    def nom(self) -> str:
        return self._nom
    
    @property
    def code_postal(self) -> int:
        return self._code_postal
        
    @property
    def habitants(self) -> int:
        return self._habitants
    
    @habitants.setter
    def habitants(self, nouveaux_habitants : int) -> None:
        self._habitants = nouveaux_habitants
    
    
    
if __name__ == '__main__':
    paris = Ville("Paris", 75000, 2_610_000)
    print(paris)
    
    paris.habitants -= 5000000
    print(paris.habitants)