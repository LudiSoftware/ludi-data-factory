from dataclasses import dataclass
import datetime


@dataclass
class Player:
    team: str                   #
    season: str
    player_first_name: str
    player_last_name: str
    gender: str
    birth_date: datetime.date
    position: str               #
    number: int                 #
    foot: str                   #
    parent1_email: str
    parent1_first_name: str
    parent1_last_name: str
    parent1_mobile_number: str
    parent2_email: str
    parent2_first_name: str
    parent2_last_name: str
    parent2_mobile_number: str
    street: str
    city: str
    state: str
    zip: str
