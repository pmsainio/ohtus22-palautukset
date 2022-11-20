from reader import PlayerReader

class PlayerStats():
    def __init__(self, reader):
        self.stats = reader.read()
        self.stats.sort()


    def top_scorers_by_nationality(self, nat:str):
        list = []
        for player in self.stats:
            if player.nationality == nat:
                list.append(player)
        return list
