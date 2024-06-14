


class Ville:
    def __init__(self, nom : str, code_postal : int, habitants : int) -> None:
        self.__nom = nom 
        self.__code_postal = code_postal
        self.__habitants = habitants
        
        
    def __str__(self) -> str:
        return f"La ville de {self.nom} se situe dans le {self.code_postal} et possède {self.habitants} habitants"
    
    
    @property
    def nom(self) -> str:
        return self.__nom
    
    @property
    def code_postal(self) -> int:
        return self.__code_postal
        
    @property
    def habitants(self) -> int:
        return self.__habitants
    
    @habitants.setter
    def habitants(self, nouveaux_habitants : int) -> None:
        self.__habitants = nouveaux_habitants
    
    
    
if __name__ == '__main__':
    paris = Ville("Paris", 75000, 2_610_000)
    print(paris)
    
    paris.habitants -= 500_000
    print(paris.habitants)