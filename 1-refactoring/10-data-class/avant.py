from dataclasses import dataclass
from enum import Enum, auto 
from datetime import datetime


class Permissions(Enum):
    pass


@dataclass
class Membre:
    pseudo : str 
    date_arrivee : datetime
    permissions : list[Permissions]