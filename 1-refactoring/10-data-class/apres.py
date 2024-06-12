from dataclasses import dataclass
from enum import Enum, auto 
from datetime import datetime


class Permission(Enum):
    READ_MESSAGES = auto()
    WRITE_MESSAGES  = auto()


@dataclass
class Member:
    _pseudo : str 
    _date_arrivee : datetime
    _permissions : list[Permission]
    
    
    @property
    def pseudo(self) -> str:
        return self._pseudo 
    
    
    @pseudo.setter
    def pseudo(self, nouveau : str) -> None:
        pass 
    
    
    @property
    def date_arrivee(self) -> datetime:
        return self._date_arrivee
    
    
    @property
    def permissions(self) -> list[Permission]:
        return self._permissions
    
    
    def add_permission(self, permission : Permission) -> None:
        if not permission is self.permissions:
            self._permissions.append(permission)
            
    
    def add_permissions(self, permissions : list[Permission]) -> None:
        for permission in permissions:
            self.add_permission(permission)
            
            
    def remove_permission(self, permission : Permission) -> None:
        if permission in self.permissions:
            self._permissions.remove(permission)
            
    
    def remove_permissions(self, permissions : list[Permission]) -> None:
        for permission in permissions:
            self.remove_permission(permission)
            
    
    def has_permission(self, permission : Permission) -> bool:
        return permission in self.permissions
            
            
    @classmethod
    def create_basic_user(cls, pseudo : str) -> "Member":
        return cls(
            pseudo,
            datetime.now(),
            [Permission.READ_MESSAGES, Permission.WRITE_MESSAGES]
        )
        
        
        
member = Member.create_basic_user("Dave") 
print(member.permissions, member.has_permission(Permission.READ_MESSAGES))
print(member.date_arrivee)
member.remove_permission(Permission.WRITE_MESSAGES)
print(member.permissions)