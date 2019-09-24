# pylint: disable=missing-docstring,too-few-public-methods

import string
from random import choice

class Game():

    def __init__(self):
        self.grid = [choice(string.ascii_uppercase) for x in range(9)]

#        return len(word) > 0 and set(word).issubset(self.grid)
    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True
