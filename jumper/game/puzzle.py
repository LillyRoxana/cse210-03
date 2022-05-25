import random
import os
#from game.parachute import parachute
import game.word_list

class Puzzle:

    def __init__(self):
        """Constructs a new Jumper/player.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._letter = input("Please choose a letter [a-z] ")
        print("you chose the letter ", self._letter)
        self._spaces = list(len(self._letter) * '_')
        self._winner = False
        self._loser = False
        self._attempt = 0
        self._guessing = ""
        
    def get_letter(self, letter):
        """Gets the current letter.
        
        Returns:
            letter: The current letter
        """
        #return self._letter
        return input(letter)
    
    def show_letters(self):
        """provides/displays the letter indicated/requested

        Args:
            self (Jumper): An instance of Jumper.
            letter (int): The given letter.
        """
        print(self._guessing)
        
    def get_try(self):
        
        if self._attempt == 0:
            self.puzzle_attempt1()
        elif self._attempt == 1:
            self.puzzle_attempt2()
        elif self._attempt == 2:
            self.puzzle_attempt3()
        elif self._attempt == 3:
            self.puzzle_attempt4()
        elif self._attempt == 4:      
            self.puzzle_attempt5()
        elif self._attempt == 5:       #I am no too sure if is "else" or "elif"
            self.puzzle_attempt6()
        
            
    def puzzle_attempt1() :
        
        print()        
        print("       _____        ")     
        print("      /_____\       ") 
        print("      \     /       ")
        print("       \   /        ")
        print("        \ /         ")
        print("         O          ")
        print("        /|\         ")
        print("        / \         ")
        print("   ^^^^^^^^^^^^^    ")
           
    def puzzle_attempt2() :
         
        print()        
        print("                    ")     
        print("      /_____\       ") 
        print("      \     /       ")
        print("       \   /        ")
        print("        \ /         ")
        print("         O          ")
        print("        /|\         ")
        print("        / \         ")
        print("   ^^^^^^^^^^^^^    ")    
        
    def puzzle_attempt3() :
        
        print()        
        print("                    ")     
        print("                    ") 
        print("      \     /       ")
        print("       \   /        ")
        print("        \ /         ")
        print("         O          ")
        print("        /|\         ")
        print("        / \         ")
        print("   ^^^^^^^^^^^^^    ")   
    
    def puzzle_attempt4() :
        
        print()        
        print("                    ")     
        print("                    ") 
        print("                    ")
        print("       \   /        ")
        print("        \ /         ")
        print("         O          ")
        print("        /|\         ")
        print("        / \         ")
        print("   ^^^^^^^^^^^^^    ")       
        
    
    def puzzle_attempt5() :
    
        print()        
        print("                    ")     
        print("                    ") 
        print("                    ")
        print("                    ")
        print("        \ /         ")
        print("         O          ")
        print("        /|\         ")
        print("        / \         ")
        print("   ^^^^^^^^^^^^^    ")  

    def puzzle_attempt6() :
    
        print()        
        print("                    ")     
        print("                    ") 
        print("                    ")
        print("                    ")
        print("                    ")
        print("         X          ")
        print("        /|\         ")
        print("        / \         ")
        print("   ^^^^^^^^^^^^^    ")  

    
    # TODO
    # make the methods/functions actually do stuff

    #def watch_jumper(self,blah):
        #pass

    #def get_hint(self):
        #pass

    #def is_found(self):
     #   pass
