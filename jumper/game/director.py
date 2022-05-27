from game.jumper import Jumper
from game.puzzle import Puzzle
from game.parachute import Parachute
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
        """ # open the word_list.txt and pick a random word
        self._word_list = open(os.path.join(DATA_DIR,'word_list.txt'),'r')
        self._word_list = self._word_list.readlines()
        self.random_word = random.choice(self._word_list)
        print(self.random_word)
        # scramble the random word and rewrite it as _____
        self._scrambled_word = ""
        self._scrambled_word = (len(self.random_word) -1 ) * "_"
        print("Your word is " + self._scrambled_word)
        print() """

        self._puzzle = Puzzle()
        self._is_playing = True
        self._jumper = Jumper()
        self._parachute = Parachute()
        self._puzzle_word = ""
        self._attempt = 0
        self._status = 0
        #self._terminal_service = Terminal_service()
        # print random_word for testing
        #print(self._random_word)


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        print("Welcome to Jumper Game!!!")
        self._puzzle.random_word()
        self._puzzle_word = self._puzzle.get_word()
        self.line = self._jumper.get_letters(self._puzzle_word)#Print the same number of lines of the words. 
        print(self.line)
        self._parachute.show_parachute(5)
        self.new_letter=''
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            if self._status == 5:
                self._is_playing = False
                return 
      
    def _get_inputs(self):
        """Moves the player to a new letter space.

        Args:
            self (Director): An instance of Director.
        """
        
        # get_letter is in Puzzle.py
        # add_letter is in Jumper.py
        
        self.new_letter = self._puzzle.get_letter("\nGuess a letter [a-z], please: ")
        self.test = self._jumper.add_letter(self.new_letter,self._puzzle_word)
        if self.test == True:
            print("Your Guess was Correct!!!")
            self._attempt = self._attempt
            print (self._attempt)
            self._puzzle.get_try(self._attempt)
        else:
            print("Sorry, Try again!!!")
            self._attempt = self._attempt + 1
            print(self._attempt)
            self._puzzle.get_try(self._attempt)

        
        #new_letter = self._terminal_service.read_letter("\nGuess a letter [a-z]: ")
        #new_letter = self._terminal_service.read_word("\nEnter a letter: ")
        """ this_letter = self._puzzle.get_letter()
        if this_letter == "":
            print("You did not choose a letter.")
            self._get_inputs()
        print("You have guessed " + this_letter)
        self.find_letter_in_word(this_letter) """

    def _do_updates(self):
        pass

    def _do_outputs(self):
         """Provides a hint for the player to use.

        Args:
             self (Director): An instance of Director.
         """
        # self._puzzle.show_letters()
        # self._puzzle.get_try()

        # self._keep_playing = self.random_word.letter_found(self._guess_player._word)
        





    # def find_letter_in_word(self,this_letter):
    #     letter_position = self.random_word.find(this_letter) + 1
    #     print(letter_position)

    #     #new_letter = self._puzzle.get_letter()
    #     #print(new_letter)

    #     #self._jumper.add_letter(new_letter)
        

        
    # def _do_updates(self):
    #     """Keeps watch on where the player/jumper is moving.

    #     Args:
    #         self (Director): An instance of Director.
    #     """
        
    #     #self._puzzle._guessing = self._random_word.compare(self._jumper) this works with word_list.py
    #     #self._puzzle._attempt = self._random_word_list.lets_to_count_attempts(self._jumper)
    #     print(self._jumper._letters)
    #     for letter in self._puzzle_word:
    #         if self.new_letter in self._puzzle_word:
    #             pass
                
                
                
    #     #self._status = self._puzzle._attempt
    #     self._status = self._puzzle._attempt
        
        
    
        
