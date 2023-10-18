from dataclasses import dataclass, field
from enum import Enum


def get_list_players() -> list:
    return ['Питон',
            'Джулс',
            'Вендетта',
            'Инкогнито',
            'Мама',
            'Камень',
            'Эмоционал',
            'Киндер',
            'Ювента',
            'СОБР']


@dataclass
class ActiveRoles:
    sheriff: int = None
    don: int = None
    mafia: list = field(default_factory=list)

@dataclass
class Days:
    nomination: list = field(default_factory=list)
    voted: list = field(default_factory=list)

@dataclass
class Nights:
    murder: int = None
    don_check: int = None
    sheriff_check: int = None

@dataclass
class GameSession:
    players: list = field(default_factory=list)
    active_roles: ActiveRoles = field(default_factory=ActiveRoles)
    best_move: list = field(default_factory=list)
    days: Days = field(default_factory=Days)
    nights: Nights = field(default_factory=Nights)


class RoleEnum(str, Enum):
    SHERIFF = 'sheriff'
    DON = 'don'
    MAF = 'mafia'
