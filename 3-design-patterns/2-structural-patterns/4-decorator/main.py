from typing import Protocol


class Notification(Protocol):
    def send(self, message : str) -> None: ...
    
    
class EmailNotification(Notification):
    def send(self, message : str) -> None:
        print(f"Sending email: {message}")


class SMSNotification(Notification):
    def send(self, message : str) -> None:
        print(f"Sending SMS: {message}")


class PushNotification(Notification):
    def send(self, message : str) -> None:
        print(f"Sending push notification: {message}")
        
        
        
class BaseNotificationDecorator(Notification):
    def __init__(self, wrapped : Notification) -> None:
        self.__wrapped = wrapped
        
    
    def send(self, message : str) -> None:
        self.__wrapped.send(message)
        



class LoggingDecorator(BaseNotificationDecorator):
    def send(self, message: str) -> None:
        print(f'Logging : "{message}"')
        return super().send(message)

        
        
if __name__ == '__main__':
    logged_email = LoggingDecorator(EmailNotification())
    logged_email.send("Je suis un email de test")