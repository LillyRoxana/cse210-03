import random
from game.list_words import list_words
from game.parachute import parachute

class Jumper:
    """The person who seeks to decipher the Puzzle. 
    
    The responsibility of a jumper/player is to keep a record of the letters 
    he/she has given and the attempts he/she has made (whether these have been correct or incorrect).
    
    Attributes:
        letter (int): The letter proposed by the jumper/player (a-z).
        attempt (List[int]): The attempts given.
    """

    def __init__(self):
        """Constructs a new Jumper/player.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._letter = list_words
        self._attempt = 5
        self._winner = False
        self._loser = False
        self._show = 
        self._guessing = ""
        
    def get_letter(self):
        """Gets the current letter.
        
        Returns:
            letterr: The current letter,
        """
        return self._letter
        
    def move_letter(self, letter):
        """provides the letter indicated/requested

        Args:
            self (Jumper): An instance of Jumper.
            letter (int): The given letter.
        """
        self._letter = letter
