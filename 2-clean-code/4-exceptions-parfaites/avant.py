from dataclasses import dataclass


@dataclass
class User:
    identifiant : int 
    email : str 
    password : str 
    
    
    
def get_user(users : list[User], identifiant : int) -> User:
    for user in users:
        if user.identifiant == identifiant:
            return user 
        
    raise ValueError


def connect(users : list[User], user_id : int) -> User:
    try:
        user = get_user(users, user_id)
        print("Connecté avec succès !")

        return user 
    except ValueError as e:
        print(e)
    
    



if __name__ == '__main__':
    database : list[User] = [
        User(1, "john@gmail.com", "1234"),
        User(2, "Jane@gmail.com", "5678"),
        User(3, "paul@gmail.com", "abcd")
    ]
    
    connect(database, 4)