from player import Player
import requests

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()
        self.list = []

    def read(self):
        for player_dict in self.response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists']
            )

            self.list.append(player)

        return self.list
