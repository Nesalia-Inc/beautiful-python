from dataclasses import dataclass
from typing import Optional


class UserConnectionError(AttributeError):
    def __init__(self, message : Optional[str] = None) -> None:
        if message is None:
            message = "Une erreur s'est produite lors de la connexion de l'utilisateur"
            
        super().__init__(message)


class IncorrectUserIdError(UserConnectionError):
    def __init__(self, message : Optional[str] = None, identifiant : Optional[int] = None) -> None:
        if message is None:
            message = f'L\'idenfiant "{identifiant}" est incorrect.'
        
        super().__init__(message)
        self.identifiant = identifiant


@dataclass
class User:
    identifiant : int 
    email : str 
    password : str 
    
    
    
database : list[User] = [
    User(1, "john@gmail.com", "1234"),
    User(1, "Jane@gmail.com", "5678"),
    User(3, "paul@gmail.com", "abcd")
]


def get_user(users : list[User], identifiant : int) -> User:
    for user in users:
        if user.identifiant == identifiant:
            return user 
        
    raise IncorrectUserIdError(identifiant=identifiant)


def connect(users : list[User], user_id : int) -> User:
    try:
        user = get_user(users, user_id)
    except IncorrectUserIdError as e:
        raise UserConnectionError from e 
    else:
        print("Connecté avec succès !")

    return user 


if __name__ == '__main__':
    print(connect(database, 4))