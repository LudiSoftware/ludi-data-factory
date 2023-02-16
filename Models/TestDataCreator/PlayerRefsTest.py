import random

from Models.Users.Player import PlayerRef


def generate_name():
    return str(random.choice(firstNames) + " " + random.choice(lastNames))


def generate_player_refs(num_players):
    player_refs = []
    for i in range(num_players):
        name = random.choice(firstNames) + " " + random.choice(lastNames)
        rank = i + 1
        player_refs.append(PlayerRef({"name": name, "rank": rank}))
    return player_refs


test = generate_player_refs(100)
print(test)