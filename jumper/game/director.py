from game.jumper import Jumper
from game.puzzle import Puzzle
from game.terminal_service import Terminal_service

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
        self._puzzle = Puzzle()
        self._keep_playing = True
        self._jumper = Jumper()
        self._status = 0
        self._terminal_service = Terminal_service()
        self._word_list = word_list()

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
        
        new_letter = self._puzzle.get_letter("\nGuess a letter [a-z], please: ")
        self._jumper.add_letter(new_letter)
        
        
        #new_letter = self._terminal_service.read_letter("\nGuess a letter [a-z]: ")
        #new_letter = self._terminal_service.read_word("\nEnter a letter: ")
        #self._jumper.add_letter(new_letter)
       
    def _do_updates(self):
        """Keeps watch on where the player/jumper is moving.

        Args:
            self (Director): An instance of Director.
        """
        
        self._puzzle._guessing = self._word_list.
        
        #self._puzzle.watch_jumper(self._jumper)
        #self._status = self._status +1
        # print some things so we can tell where we are
        #print(self._status)
        #print("we are in the _do_updates() method")
        
    def _do_outputs(self):
        """Provides a hint for the player to use.

        Args:
            self (Director): An instance of Director.
        """
        
        
        
        #hint = self._puzzle.get_hint()
        #self._terminal_service.write_text(hint)
        #if self._puzzle.is_found():
        #    self._keep_playing = False
