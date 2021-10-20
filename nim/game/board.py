import random

class Board:
    """This class is where the board is created and manipulated."""

    def __init__(self):

        self._piles = []
        self._prepare()

    def apply(self, move):
        
        pile = move.get_pile()
        stones = move.get_stones()
        self._piles[pile] = max(0, self._piles[pile] - stones)

    def to_string(self):

        text = "\n- - - - - - - - - - - - - - "
        for pile, stones in enumerate(self._piles):
            text += (f"\n{pile}: " + "O " * stones)
        text += "\n- - - - - - - - - - - - - - "
        return text
    def _prepare(self):

        piles = random.randint(2, 5)
        for n in range (piles):
            stones = random.randint(1,9)
            self._piles.append(stones)

    def is_empty(self):

        empty = [0] * len(self._piles)
        return self._piles == empty