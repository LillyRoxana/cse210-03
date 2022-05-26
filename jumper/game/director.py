from game.jumper import Jumper
from game.puzzle import Puzzle
from game.terminal_service import Terminal_service
from game import ROOT_DIR,DATA_DIR
import os
import random

class Director:
    
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        jumper (Jumper): The game's jumper.
        is_playing (boolean): Whether or not to keep playing.
        puzzle (Puzzle): The game's puzzle.
        terminal_service: For getting and displaying information on the terminal.
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        # open the word_list.txt and pick a random word
        self._word_list = open(os.path.join(DATA_DIR,'word_list.txt'),'r')
        self._word_list = self._word_list.readlines()
        self.random_word = random.choice(self._word_list)
        # scramble the random word and rewrite it as _____
        self._scrambled_word = ""
        self._scrambled_word = (len(self.random_word) -1 ) * "_"
        print()
        print("Your word is " + self._scrambled_word)
        print()

        self._puzzle = Puzzle(self.random_word)
        self._keep_playing = True
        self._jumper = Jumper()


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            if self._status == 5:
                self._keep_playing = False
                return 
      
            
    def _get_inputs(self):
        """Moves the player to a new letter space.

        Args:
            self (Director): An instance of Director.
        """
        
        # get_letter is in Puzzle.py
        # add_letter is in Jumper.py
        
        new_letter = self._puzzle.get_letter()
        self._jumper.add_letter(new_letter)
        
        
    def _do_updates(self):
        """Keeps watch on where the player/jumper is moving.

        Args:
            self (Director): An instance of Director.
        """
        
        self._status = self._puzzle._attempt
        
        
    def _do_outputs(self):
        """Provides a hint for the player to use.

        Args:
            self (Director): An instance of Director.
        """
        self._puzzle.show_letters()
        self._puzzle.get_try()

        self._keep_playing = self.random_word.letter_found(self._guess_player._word)
        
        
