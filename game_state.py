RED_SCORE = 2
BLUE_SCORE = 3

class GameState:
    def __init__(self, red, blue, is_misere):
        self.red = red
        self.blue = blue
        self.is_misere = is_misere

    def is_game_over(self):
        return self.red == 0 or self.blue == 0

    def get_score(self):
        return self.red * RED_SCORE + self.blue * BLUE_SCORE

    def clone(self):
        return GameState(self.red, self.blue, self.is_misere)