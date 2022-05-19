from game.jumper import Jumper
from game.puzzle import Puzzle
from game.terminal_service import Terminal_service
from game.list_words import List_words

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
        self._terminal_service = Terminal_service()

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            
     def _get_inputs(self):
        """Moves the player to a new letter space.

        Args:
            self (Director): An instance of Director.
        """
        new_letter = self._terminal_service.read_word("\nEnter a letter: ")
        self._jumper.move_letter(new_letter)
        ---------
    def _do_updates(self):
        """Keeps watch on where the player/jumper is moving.

        Args:
            self (Director): An instance of Director.
        """
        self._puzzle.watch_jumper(self._jumper)
        
    def _do_outputs(self):
        """Provides a hint for the player to use.

        Args:
            self (Director): An instance of Director.
        """
        hint = self._puzzle.get_hint()
        self._terminal_service.write_text(hint)
        if self._puzzle.is_found():
            self._keep_playing = False
