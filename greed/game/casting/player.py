from game.casting.actor import Actor

# TODO: Implement the Player class here. Don't forget to inherit from Actor!
class Player(Actor):

    def __init__(self):
        self._score = 0

    def score_rock(self):
        self._score -= 1

    def score_tnt(self):
        self._score -= 10

    def score_gem(self):
        self._score += 1

    def score_emerald(self):
        self._score += 2

    def score_ruby(self):
        self._score += 5

    def score_diamond(self):
        self._score += 10

    def get_score(self):
        return(self._score)

