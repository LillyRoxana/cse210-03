import random
import os
from game.parachute import parachute

class Puzzle:

    def __init__(self):
        """Constructs a new Jumper/player.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._letter = input("Please choose a letter [a-z] ")
        self._word_list = open("game/word_list.txt","r")
        self._words = self._word_list.readlines()
        self._word = random.choice(self._words)
        print(self._word)
        self._spaces = list(len(self._letter) * '_')
        self._winner = False
        self._loser = False
        self._attempt = 5
        self._guessing = ""
        
    def get_letter(self, letter):
        """Gets the current letter.
        
        Returns:
            letter: The current letter
        """
        return self._letter
        
    def show_letters(self):
        """provides/displays the letter indicated/requested

        Args:
            self (Jumper): An instance of Jumper.
            letter (int): The given letter.
        """
        print(self._guessing)

    # TODO
    # make the methods/functions actually do stuff

    def watch_jumper(self,blah):
        pass

    def get_hint(self):
        pass

    def is_found(self):
        pass
