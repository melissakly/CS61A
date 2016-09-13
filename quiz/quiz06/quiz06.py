def make_test_random():
    """A deterministic random function that cycles between
    [0.0, 0.1, 0.2, ..., 0.9] for testing purposes.

    >>> random = make_test_random()
    >>> random()
    0.0
    >>> random()
    0.1
    >>> random2 = make_test_random()
    >>> random2()
    0.0
    """
    rands = [x / 10 for x in range(10)]
    def random():
        rand = rands[0]
        rands.append(rands.pop(0))
        return rand
    return random

random = make_test_random()

### Phase 1: The Player Class
class Player:
    """
    >>> random = make_test_random()
    >>> p1 = Player('Hill')
    >>> p2 = Player('Don')
    >>> p1.popularity
    100
    >>> p1.debate(p2)  # random() should return 0.0
    >>> p1.popularity
    150
    >>> p2.popularity
    100
    >>> p2.votes
    0
    >>> p2.speech(p1)
    >>> p2.votes
    10
    >>> p2.popularity
    110
    >>> p1.popularity
    135

    """
    def __init__(self, name):
        self.name = name
        self.votes = 0
        self.popularity = 100

    def debate(self, other):
        p1 = self.popularity
        p2 = other.popularity
        probability = max(0.1, p1 / (p1 + p2))
        if random() < probability:
            self.popularity += 50
        else:
            self.popularity -= 50
        if self.popularity < 0:
            self.popularity = 0

    def speech(self, other):
        p1 = self.popularity
        p2 = other.popularity
        self.votes += p1 // 10
        self.popularity += p1 // 10
        other.popularity -= p2 // 10
        if p2 <0:
            p2 = 0

    def choose(self, other):
        return self.speech


### Phase 2: The Game Class
class Game:
    """
    >>> p1, p2 = Player('Hill'), Player('Don')
    >>> g = Game(p1, p2)
    >>> winner = g.play()
    >>> p1 is winner
    True

    """
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.turn = 0

    def play(self):
        while not self.game_over:
            if self.turn % 2 == 0:
                self.p1.choose(self.p2)(self.p2)
            elif self.turn % 2 == 1:
                self.p2.choose(self.p1)(self.p1)
            self.turn += 1
        return self.winner

    @property
    def game_over(self):
        return max(self.p1.votes, self.p2.votes) >= 50 or self.turn >= 10

    @property
    def winner(self):
        if self.p1.votes > self.p2.votes:
            return self.p1
        elif self.p2.votes < self.p1.votes:
            return self.p2
        else:
            return None


### Phase 3: New Players
class AggressivePlayer(Player):
    """
    >>> random = make_test_random()
    >>> p1, p2 = AggressivePlayer('Don'), Player('Hill')
    >>> g = Game(p1, p2)
    >>> winner = g.play()
    >>> p1 is winner
    True

    """
    def choose(self, other):
        p1 = self.popularity
        p2 = other.popularity
        if p1 <= p2:
            return self.debate
        else:
            return self.speech

class CautiousPlayer(Player):
    """
    >>> random = make_test_random()
    >>> p1, p2 = CautiousPlayer('Hill'), AggressivePlayer('Don')
    >>> p1.popularity = 0
    >>> p1.choose(p2) == p1.debate
    True
    >>> p1.popularity = 1
    >>> p1.choose(p2) == p1.debate
    False

    """
    def choose(self, other):
        if self.popularity == 0:
            return self.debate
        else:
            return self.speech
