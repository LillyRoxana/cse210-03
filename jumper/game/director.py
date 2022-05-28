from game.puzzle import Puzzle
from game.word_generator import word_list
from game.jumper import Jumper

class Director:

    def __init__(self):
        
        self._word_generator = word_list()
        self._is_playing = True
        self._jumper = Jumper()
        self._puzzle = Puzzle()
        
    def start_new_game(self):
        print("Welcome to Jumper!\nThe rules are simple: guess the word\nbefore you spend your lifes\nAre you ready?")
        self._puzzle.puzzle()
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            if self._status == 4:
                
                self._is_playing = False
                return

    def _get_inputs(self):
        
        new_guess = self._puzzle.get_letter("\nHi! Please type a letter: ")
        if new_guess.isalpha()==True:
            self._jumper.add_letter(new_guess)
        else:
            print("Sorry that is not a valid input!!!\nUse letters only")
            self._get_inputs()
        
    def _do_updates(self):
        
        self._puzzle._guessing = self._word_generator.lets_to_compare_letters(self._jumper)
        self._puzzle._attempt = self._word_generator.lets_to_count_attempts(self._jumper)

        self._status = self._puzzle._attempt
        
    def _do_outputs(self):
        
        self._puzzle.show_letter()
        self._puzzle.get_attempt()

        self._is_playing = self._word_generator.is_found(self._jumper._letters)
