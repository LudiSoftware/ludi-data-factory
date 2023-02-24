import random
from Models.TestDataCreator.TestData import firstNames, lastNames
from Models.Users.Player import PlayerRef
import uuid

def generate_name():
    return str(random.choice(firstNames) + " " + random.choice(lastNames))

def generate_player(rank=1):
    player = PlayerRef()
    player.id = str(uuid.uuid1())
    player.name = generate_name()
    player.rank = 1
    player.playerId = str(uuid.uuid1())
    return player

def generate_roster(num_players):
    player_refs = []
    for i in range(num_players):
        newPlayerRef = PlayerRef()
        player_refs.append(newPlayerRef.__dict__)
    return player_refs

def generate_team():
    pass

def generate_tryout():
    pass

if __name__ == '__main__':
    test = generate_roster(20)
    print(test)