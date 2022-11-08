from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    Points = 1
    Goals = 2
    Assists = 3


def sort_by_points(player):
    return player.points


class Statistics:
    def __init__(self, reader=PlayerReader()):

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, by=SortBy.Points):
        sort_criteria = {
            SortBy.Points: lambda p: p.points,
            SortBy.Goals: lambda p: p.goals,
            SortBy.Assists: lambda p: p.assists
        }
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_criteria[by]
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
