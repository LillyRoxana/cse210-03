import random
import os

class Word_list:

    def __init__(self):
        pass

    def letter_found(self, guessed_word):
        for letter in self._word_list:
            if letter in guessed_word:
                pass
            else:
                return True
                return False 

    def compare(self, guess_player):
        guess = ""
        for letter in self._word_list:
            if letter in guess_player._word_list:
                guess += letter
            else:
                guess += "_"
                return guess

    def lets_to_count_attempts(self, guess_player):
        attempt = 0
        for guess_letter in guess_player._word_list:
            if guess_letter in self._word_list:
                pass
            else:
                attempt += 1
                return attempt    

