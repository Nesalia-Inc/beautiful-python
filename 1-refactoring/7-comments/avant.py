



# Définition de la classe Personne
class Personne:
    # Constructeur de la classe Personne
    def __init__(self, nom : str, age : int) -> None:
        # Initialise l'attribut nom
        self.nom = nom
        # Initialise l'attribut age
        self.age = age

    # Méthode pour afficher les informations de la personne
    def afficher_info(self) -> None:
        # Affiche le nom de la personne
        print(f"Nom: {self.nom}")
        # Affiche l'âge de la personne
        print(f"Âge: {self.age}")

# Création d'une instance de la classe Personne
personne = Personne("Alice", 30)
# Appel de la méthode pour afficher les informations de la personne
personne.afficher_info()
