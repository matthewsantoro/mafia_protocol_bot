from dataclasses import dataclass
from typing import NamedTuple


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
class ActiveRoles(NamedTuple):
    sheriff: int = None
    don: int = None
    mafia: set = None



@dataclass
class GameSession:
    players: list
    active_roles: ActiveRoles = ActiveRoles()
    best_move: list = None
    days: list = None
    nights: list = None
