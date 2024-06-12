from dataclasses import dataclass


@dataclass
class User:
    id : int 
    name : str 


def get_user_by_id(database : list[User], id : int):
    for user in database:
        if user.id == id:
            return user 
        
    raise ValueError("User not found")


def get_user_by_name(database : list[User], name : str):
    for user in database:
        if user.name == name:
            return user 
        
    raise ValueError("User not found")


def add_new_user(database : list[User], user : User) -> list[User]:
    if user in database:
        raise ValueError
    
    new_database = list(database)
    new_database.append(user)
    return new_database


def remove_user(database : list[User], user : User) -> list[User]:
    if not (user in database):
        raise ValueError
    
    new_database = list(database)
    new_database.remove(user)
    return new_database



def is_user_in_database(database : list[User], user : User) -> bool:
    return user in database


if __name__ == '__main__':
    database : list[User] = [
        User(1, "Jean"),
        User(2, "Jeanne")
    ]
    
    database = add_new_user(database, User(3, "John"))
    print(get_user_by_name(database, "John"))
