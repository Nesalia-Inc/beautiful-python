

class Personne: 
    def __init__(self, nom : str, prenom : str, age : int) -> None:
        self.__nom = nom 
        self.__prenom = prenom 
        self.__age = age 
    
    
    def __str__(self) -> str:
        return f'Personne(nom="{self.nom}", prenom="{self.prenom}", age={self.age})'
    
    
    @property
    def nom(self) -> str:
        return self.__nom 
    
    
    @property
    def prenom(self) -> str:
        return self.__prenom
    
    
    @property
    def age(self) -> int:
        return self.__age
    
    
    def __check_nom(self, nom : str) -> bool:
        return len(nom) >= 2 and len(nom) <= 20
    
    def __check_prenom(self, prenom : str) -> bool:
        return self.__check_nom(prenom)
    
    def __check_age(self, age : int) -> bool:
        return age >= 0
    
    
    @classmethod
    def create(cls, nom : str, prenom : str, age : int) -> "Personne":
        obj = cls(nom, prenom, age)
        
        if any([not obj.__check_nom(nom), not obj.__check_prenom(prenom), not obj.__check_age(age)]):
            raise ValueError("Un des paramètres ne correspond pas aux règles de la classe")
        
        return obj 
    
    
    
    
    
if __name__ == '__main__':
    personne = Personne.create("Jean", "Doe", 45)
    
    print(personne)