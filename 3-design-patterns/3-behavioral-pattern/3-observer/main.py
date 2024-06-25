import email
from typing import Protocol


class Observer(Protocol):
    def update(self, message : str) -> None: ...
    
    
class Subject(Protocol):
    observers : list[Observer]
    
    def register(self, observer : Observer) -> None: ...
    def remove(self, observer : Observer) -> None: ...
    def notify(self, message : str) -> None: ...
    
    
    
class EmailService(Subject):
    def __init__(self) -> None:
        self.observers : list[Observer] = []
        
    def register(self, observer: Observer) -> None:
        self.observers.append(observer)
        
    def remove(self, observer: Observer) -> None:
        return self.observers.remove(observer)
    
    def notify(self, message: str) -> None:
        for observer in self.observers:
            observer.update(message)
    
    def send_email(self, message : str) -> None:
        print(f"Sending email: {message}")
        self.notify(message)
        
        
class User(Observer):
    def __init__(self, name : str) -> None:
        self.name = name
    
    def update(self, message : str) -> None:
        print(f"{self.name} received message: {message}")


if __name__ == '__main__':
    email_service = EmailService()
    users = [User("Alice"), User("Bob"), User("Charlie")]
    
    for user in users:
        email_service.register(user)
        
    email_service.send_email("Je suis un premier email.")
    
    email_service.remove(users[1])
    
    print("-------------")
    
    email_service.send_email("Je suis un second email.")
    
    