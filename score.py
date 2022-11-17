class Score():

    def __init__(self):
        self.score_x = 0
        self.score_o = 0

    def increase_score(self, piece):
        if piece == 'X':
            self.score_x += 1
        else:
            self.score_o += 1
