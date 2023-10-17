from dataclasses import dataclass, field


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
class ActiveRoles():
    sheriff: int = None
    don: int = None
    mafia: set = None



@dataclass
class GameSession:
    players: list
    active_roles: ActiveRoles = field(default_factory=ActiveRoles)
    best_move: list = None
    days: list = None
    nights: list = None

