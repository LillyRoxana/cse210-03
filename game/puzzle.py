import random
from game.list_words import list_words
from game.parachute import parachute

class Puzzle:

    def __init__(self):
        """Constructs a new Jumper/player.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._letter = list_words
        self._attempt = 0
        self._guessing = ""
        
    def get_letter(self, letter):
        """Gets the current letter.
        
        Returns:
            letter: The current letter
        """
        return self._letter
        
    def move_letter(self):
        """provides/displays the letter indicated/requested

        Args:
            self (Jumper): An instance of Jumper.
            letter (int): The given letter.
        """
        print(self._guessing)
