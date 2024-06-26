


class Personne:
    def __init__(self, nom : str, age : int) -> None:
        self.nom = nom
        self.age = age

    def afficher_info(self) -> None:
        print(f"Nom: {self.nom}")
        print(f"Age: {self.age}")



class PersonneFactory:
    """
    Utilisation de la méthode de fabrique pour créer des instances de Personne.
    Cela permet de centraliser la logique de création et de potentiellement ajouter
    des fonctionnalités supplémentaires comme la validation des données ou le logging.
    """
    
    @staticmethod
    def creer_personne(nom : str, age : int) -> Personne:
        # TODO: Ajouter la validation des données ici
        if len(nom) < 2:
            raise ValueError("Le nom doit avoir plus d'un caractère")
        if age <= 0:
            raise ValueError("L'âge ne peut pas être nul")
        
        return Personne(nom, age)



if __name__ == '__main__':    
    personne = PersonneFactory.creer_personne("Alice", 30)
    personne.afficher_info()
