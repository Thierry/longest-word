# pylint: disable=missing-docstring,too-few-public-methods

import string
from random import choice
import requests
# API https://wagon-dictionary.herokuapp.com/:word

class Game():
    def is_in_dictionary(self, word):
        try:
            resp = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        except:
            print(f"An error occured contacting LeWagon dictionnary API ({resp.status}")
            sys.exit(1)
        return resp.json()["found"]

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
        return self.is_in_dictionary(word)
