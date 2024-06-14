from compte import Compte
from client import Client, Personne, Adresse

class Banque:
    def __init__(self) -> None:
        self._comptes : list[Compte] = []
        
    
    @property
    def comptes(self) -> list[Compte]:
        return self._comptes
    
    
    def ajouter_compte(self, personne : Personne, adresse : Adresse) -> None:
        client = Client.create(personne, adresse)
        
        compte = Compte.create(client, -100)

        self._comptes.append(compte)
        
        
    def add_compte(self, client : Client) -> None:
        self._comptes.append(Compte.create(client, -100))
    
    
    def get_user_by_code(self, code : str) -> Compte:
        return list(filter(lambda compte : compte.code == code, self.comptes))[0]

