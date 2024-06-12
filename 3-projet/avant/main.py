import random


class Client:
    def __init__(self, prenom : str, nom : str, telephone : str, numero_rue : int, rue : str, code_postal : int):
        self.prenom = prenom
        self.nom = nom 
        self.telephone = telephone
        self.numero_rue = numero_rue
        self.rue = rue 
        self.code_postal = code_postal
        
        self.identifiant = self.generer_identifiant()
        
    
    def generer_identifiant(self) -> int:
        identifiant = random.randint(100_000, 1_000_000)
            
        return identifiant
    
    
    
class Compte:
    def __init__(self, client : Client, code : str, argent : float, decouvert : float):
        self.client = client 
        self.code = code 
        self.argent = argent 
        self.decouvert = decouvert 
        
        
    def generer_nouveau_code(self):
        self.code = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        
        
        
def main() -> None:
    comptes : list[Compte] = []
    
    running = True 
    print("Bienvenue dans la banque. Veuillez choisir une option")
        
    while running:
        print("1. Accéder à votre compte")
        print("2. Créer un nouveau compte")
        print("3. Quitter")
        
        choice = int(input())
        
        if choice == 1:
            code = input("Quel est votre code de compte : ")
            for compte in comptes:
                if compte.code == code:
                    account_running = True
                    
                    while account_running:
                        print("Que voulez-vous faire avec votre compte :")
                        print("1. Ajouter de l'argent sur le compte")    
                        print("2. Retirer de l'argent du compte")    
                        print("3. Savoir l'argent que vous avez sur votre compte")
                        print("4. Créer un nouveau code")  
                        print("5. Quitter")
                        
                        account_choice = int(input())
                        
                        if account_choice == 1:
                            quantity = int(input("Quel est la quantité d'argent que vous souhaitez ajouter : "))
                            compte.argent += quantity
                            print(f"Vous venez d'ajouter {quantity}€ sur votre compte, vous avez {compte.argent}€ au total")
                        elif account_choice == 2:
                            quantity = int(input("Quel est la quantité d'argent que vous souhaitez retirer : "))
                            compte.argent -= quantity
                            print(f"Vous venez de retirer {quantity}€ sur votre compte, vous avez {compte.argent}€ au total")
                        elif account_choice == 3:
                            print(f"Vous avez actuellement {compte.argent}€ sur votre compte.")
                        elif account_choice == 4:
                            compte.code = ''.join([str(random.randint(0, 9)) for _ in range(4)])
                            print(f"Votre nouveau code est {compte}.")
                        elif account_choice == 5:
                            account_running = False 
                            
                    break
                
        elif choice == 2:
            print("Création d'un nouveau compte :")
            prenom = input("Quel est votre prénom : ")
            nom = input("Quel est votre nom : ")
            telephone = input("Quel est votre numéro de téléphone : ")
            
            numero = int(input("Quel est votre numéro de batiment : "))
            rue = input("Quel est le nom de votre rue : ")
            code_postal = int(input("Quel est votre code postal : "))
            
            client = Client(prenom, nom, telephone, numero, rue, code_postal)
            code = ''.join([str(random.randint(0, 9)) for _ in range(4)])
            compte = Compte(client, code, 0, -100)
            comptes.append(compte)
            print(compte.code)
            
        elif choice == 3:
            running = False
            
            
            
if __name__ == '__main__':
    main()