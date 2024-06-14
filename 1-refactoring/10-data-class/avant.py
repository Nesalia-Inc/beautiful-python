from dataclasses import dataclass
from enum import Enum, auto 
from datetime import datetime


class Permissions(Enum):
    READ_MESSAGES = auto()
    WRITE_MESSAGES  = auto()


@dataclass
class Membre:
    pseudo : str 
    date_arrivee : datetime
    permissions : list[Permissions]