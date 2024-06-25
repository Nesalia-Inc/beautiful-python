from __future__ import annotations

from typing import Protocol, TypeVar


T = TypeVar("T", contravariant=True)


class Mediator(Protocol[T]):
    def register(self, colleague : T) -> None: ...
    def send(self, sender : str, receiver : str, message : str) -> None: ... 
    
    
class User:
    def __init__(self, name : str, mediator : Mediator["User"]) -> None:
        self.name = name 
        self.mediator = mediator
        
        self.mediator.register(self)
        
    def send(self, receiver_name : str, message : str) -> None:
        print(f"{self.name} sends message to {receiver_name}: {message}")
        self.notify(receiver_name, message)
    
    def receive(self, message : str, sender : str) -> None:
        print(f"{self.name} received message from {sender}: {message}")
    
    def notify(self, receiver_name : str, message : str) -> None:
        self.mediator.send(self.name, receiver_name, message)
        
    
    
class ChatServer(Mediator[User]):
    def __init__(self) -> None:
        self.users : list[User] = []
        
    def register(self, colleague: User) -> None:
        self.users.append(colleague)
        
    def send(self, sender: str, receiver: str, message: str) -> None:
        for user in self.users:
            if user.name == receiver:
                user.receive(message, sender)



if __name__ == '__main__':
    server = ChatServer()
    
    jean = User("Jean", server)
    jeanne = User("Jeanne", server)
    
    jean.send("Jeanne", "Bonjour !")

