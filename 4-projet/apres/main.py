from compte import Compte, NotEnoughMoneyError
from client import Client, Personne, Adresse
from banque import Banque

from enum import Enum, auto 


class ChoixAccueil(Enum):
    ACCEDER_COMPTE = auto()
    CREER_COMPTE = auto()
    QUITTER = auto()
    
    @classmethod
    def from_int(cls, value : int) -> "ChoixAccueil":
        return list(cls)[value - 1]
    
    
class ChoixCompte(Enum):
    AJOUTER_ARGENT = auto()
    RETIRER_ARGENT = auto()
    CONNAITRE_ARGENT = auto()
    NOUVEAU_CODE = auto()
    QUITTER = auto()
    
    @classmethod
    def from_int(cls, value : int) -> "ChoixCompte":
        return list(cls)[value - 1]


class AccountView:
    def display_account_money(self, account : Compte) -> None:
        print(f"Vous avez actuellement {account.argent}€ sur votre compte.")
        
    def display_add_money(self, account : Compte, quantity : float) -> None:
        print(f"Vous venez d'ajouter {quantity}€ sur votre compte, vous avez {account.argent}€ au total")

    def display_remove_money(self, account : Compte, quantity : float) -> None:
        print(f"Vous venez de retirer {quantity}€ sur votre compte, vous avez {account.argent}€ au total")

    def display_new_code(self, code : str) -> None:
        print(f"Votre nouveau code est {code}.")
        
    def display_limit_reached(self, account : Compte, quantity : float):
        print(f"Vous avez cherché à retirer {quantity}€ alors que vous avez {account.argent}€ sur votre compte")

    def display_account_menu(self) -> None:
        print("Que voulez-vous faire avec votre compte :")
        print("1. Ajouter de l'argent sur le compte")    
        print("2. Retirer de l'argent du compte")    
        print("3. Savoir l'argent que vous avez sur votre compte")
        print("4. Créer un nouveau code")  
        print("5. Quitter")
        
        
class AccountController:
    view = AccountView()
    
    def add_money_to_account(self, account : Compte, quantity : float) -> None:
        account.argent += quantity
        
        self.view.display_add_money(account, quantity)
        
        
    def remove_money_to_account(self, account : Compte, quantity : float) -> None:
        try:
            account.argent -= quantity
        except NotEnoughMoneyError:
            self.view.display_limit_reached(account, quantity)
        else:
            self.view.display_remove_money(account, quantity)
        
        
    def main(self, account : Compte) -> None:
        running = True
        
        while running:
            self.view.display_account_menu()
            
            choice = ChoixCompte.from_int(int(input()))
            
            if choice == ChoixCompte.AJOUTER_ARGENT:
                quantity = int(input("Quel est la quantité d'argent que vous souhaitez ajouter : "))
                self.add_money_to_account(account, quantity)
            elif choice == ChoixCompte.RETIRER_ARGENT:
                quantity = int(input("Quel est la quantité d'argent que vous souhaitez retirer : "))
                self.remove_money_to_account(account, quantity)
            elif choice == ChoixCompte.CONNAITRE_ARGENT:
                self.view.display_account_money(account)
            elif choice == ChoixCompte.NOUVEAU_CODE:
                account.generate_new_code()
                self.view.display_new_code(account.code)
            elif choice == ChoixCompte.QUITTER:
                running = False
        


class Menu:
    def create_client_from_inputs(self) -> Client:
        print("Création d'un nouveau compte :")
        prenom = input("Quel est votre prénom : ")
        nom = input("Quel est votre nom : ")
        telephone = input("Quel est votre numéro de téléphone : ")
        
        numero = int(input("Quel est votre numéro de batiment : "))
        rue = input("Quel est le nom de votre rue : ")
        code_postal = int(input("Quel est votre code postal : "))
        
        personne = Personne(prenom, nom, telephone)
        adresse = Adresse(numero, rue, code_postal)
        return Client(personne, adresse)
    
    
    def get_account_from_input_code(self, bank : Banque) -> Compte:
        code = input("Quel est votre code de compte : ")
        return bank.get_user_by_code(code)
    
    def afficher_accueil(self) -> None:
        print("1. Accéder à votre compte")
        print("2. Créer un nouveau compte")
        print("3. Quitter")
    

    def main(self, bank : Banque) -> None:
        running = True 
        print("Bienvenue dans la banque. Veuillez choisir une option")
        
        while running:
            self.afficher_accueil()
            
            choice = ChoixAccueil.from_int(int(input()))
            
            if choice == ChoixAccueil.ACCEDER_COMPTE:
                account = self.get_account_from_input_code(bank)
                AccountController().main(account)
            elif choice == ChoixAccueil.CREER_COMPTE:
                client = self.create_client_from_inputs()
                bank.add_compte(client)
            elif choice == ChoixAccueil.QUITTER:
                running = False
            


if __name__ == '__main__':
    banque = Banque()
    banque.ajouter_compte(
        Personne("Jean", "Doe", "0701020304"),
        Adresse(15, "Rue des rois", 55000)
    )
    
    print(banque.comptes[0].code)
    
    Menu().main(banque)