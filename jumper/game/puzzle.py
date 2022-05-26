import random
import os

class Puzzle:

    def __init__(self):
        """Constructs a new Jumper/player.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._winner = False
        self._loser = False
        self._attempt = 0
        self._guessing = ""
        
    def get_letter(self):
        """Gets the current letter.
        
        Returns:
            letter: The current letter
        """
        self.letter = input("Please choose a letter [a-z]: ").lower()
        return self.letter


    def show_letters(self):
        """provides/displays the letter indicated/requested

        Args:
            self (Jumper): An instance of Jumper.
            letter (int): The given letter.
        """

        
    def get_try(self):
        
        if self._attempt == 0:
            self.puzzle_attempt1()
            self.get_letter()
        elif self._attempt == 1:
            self.puzzle_attempt2()
            self.get_letter()
        elif self._attempt == 2:
            self.puzzle_attempt3()
            self.get_letter()
        elif self._attempt == 3:
            self.puzzle_attempt4()
            self.get_letter()
        elif self._attempt == 4:      
            self.puzzle_attempt5()
            self.get_letter()
        elif self._attempt == 5:       #I am no too sure if is "else" or "elif"
            self.puzzle_attempt6()
        
            
    def puzzle_attempt1(self) :
        
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

    
