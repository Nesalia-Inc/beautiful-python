

class Utilisateur:
    def __init__(self, nom : str, email : str, mdp : str, adresse : str, telephone : str) -> None:
        self._nom = nom 
        self._email = email 
        self._mdp = mdp 
        self._telephone = telephone
        
        self.adresse = adresse
        
        
        
    @property
    def nom(self) -> str:
        return self._nom
    
    @nom.setter
    def nom(self, nouveau_nom : str) -> None:
        if not nouveau_nom.isalpha():
            raise ValueError
        
        self._nom = nouveau_nom
    
    
    @property
    def email(self) -> str:
        return self._email
    
    @property
    def mdp(self) -> str:
        return self._mdp
    
    @mdp.setter
    def mdp(self, nouveau_mdp : str) -> None:
        if len(nouveau_mdp) < 8:
            raise ValueError
        
        self._mdp = nouveau_mdp
    
    @property
    def telephone(self) -> str:
        return self._telephone
    
    @telephone.setter
    def telephone(self, nouveau_telephone : str) -> None:
        if len(nouveau_telephone) != 10:
            raise ValueError
        
        self._telephone = nouveau_telephone 
    
    
        
if __name__ == '__main__':
    utilisateur = Utilisateur(
        "Jean",
        "jean@gmail.com",
        "1234",
        "18 Rue des Rois, 75000",
        "0701020304"
    )