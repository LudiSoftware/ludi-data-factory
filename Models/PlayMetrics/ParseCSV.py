import csv
from dataclasses import dataclass
from typing import List
import datetime

from Models.Users.Player import Player


# from Models.PlayMetrics.Player import Player


def parse_csv_file(file_path: str) -> List[Player]:
    players = []

    with open(file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')

        for row in reader:
            player = Player(row)
            # player = Player(
            #     team=row['team'],
            #     season=row['season'],
            #     player_first_name=row['player_first_name'],
            #     player_last_name=row['player_last_name'],
            #     gender=row['gender'],
            #     birth_date=datetime.datetime.strptime(row['birth_date'], '%Y-%m-%d').date(),
            #     position=row['position'],
            #     number=int(row['number']),
            #     foot=row['Foot'],
            #     parent1_email=row['parent1_email'],
            #     parent1_first_name=row['parent1_first_name'],
            #     parent1_last_name=row['parent1_last_name'],
            #     parent1_mobile_number=row['parent1_mobile_number'],
            #     parent2_email=row['parent2_email'],
            #     parent2_first_name=row['parent2_first_name'],
            #     parent2_last_name=row['parent2_last_name'],
            #     parent2_mobile_number=row['parent2_mobile_number'],
            #     street=row['street'],
            #     city=row['city'],
            #     state=row['state'],
            #     zip=row['zip']
            # )
            players.append(player)

    return players


if __name__ == '__main__':
    # Read and parse the CSV file
    csv_file_path = "/Users/chazzromeo/Downloads/sample.csv"
    players = parse_csv_file(csv_file_path)
    # Print the parsed players
    for player in players:
        print(player)