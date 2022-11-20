class Player:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists
        self.score = int(self.goals) + int(self.assists)
    
    def __str__(self):
        return f"{self.name:20} {self.team}, {self.goals:2} + {self.assists:2} = {self.score}"

    def __gt__(self, self_2):
        return self.score < self_2.score
