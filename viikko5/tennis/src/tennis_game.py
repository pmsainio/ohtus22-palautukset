class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score = ""

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def even_score(self):
        if self.player1_score == self.player2_score:
            if self.player1_score == 0:
                return "Love-All"
            elif self.player1_score == 1:
                return "Fifteen-All"
            elif self.player1_score == 2:
                return "Thirty-All"
            elif self.player1_score == 3:
                return "Forty-All"
            else:
                return "Deuce"
    
    def early_game_score(self, temp_score):
        if temp_score == 0:
            return "Love"
        elif temp_score == 1:
            return "Fifteen"
        elif temp_score == 2:
            return "Thirty"
        elif temp_score == 3:
            return "Forty"

    def end_game_score(self):
        difference = self.player1_score - self.player2_score
        if difference == 0:
            self.score = "deuce"

        elif abs(difference) == 1:
            self.score = "Advantage "
            if difference > 0:
                self.score += "player1"
            else:
                self.score += "player2"
        else:
            self.score = "Win for "
            if difference > 0:
                self.score += "player1"
            else:
                self.score += "player2"
        return self.score

    def get_score(self):
        if self.player1_score == self.player2_score:
            score = self.even_score()

        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.end_game_score()

        else:
            score = f"{self.early_game_score(self.player1_score)}-{self.early_game_score(self.player2_score)}"
            
        return score
