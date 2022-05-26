import random
import os
from game import ROOT_DIR,DATA_DIR

class Puzzle:

    def __init__(self):
        """Constructs a new Jumper/player.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._random_word=""
        self._f = open(os.path.join(DATA_DIR,'word_list.txt'),'r')
        self._words_list = []
        lines = self._f.read()
        self._words_list = lines.splitlines()
        self._f.close()
        #print(self._words_list)
        self._attempt = 0
    
    def random_word(self):
        #from the list select one word
        self._random_word = random.choice(self._words_list)
        print(self._random_word)
        
    def get_word(self):
        #This method will get the private random word. 
        return self._random_word
    
    def get_letter(self, letter):
        self._winner = False
        self._loser = False
        
        self._guessing = ""
        
    def get_letter(self,text):
        """Gets the current letter.
        
        Returns:
            letter: The current letter
        """
        self.letter = input(text)
        return self.letter


    def show_letters(self):
        """provides/displays the letter indicated/requested

        Args:
            self (Jumper): An instance of Jumper.
            letter (int): The given letter.
        """

        
    def get_try(self,attempt):
        
        if attempt == 0:
            self.puzzle_attempt1()
            #self.get_letter()
        elif attempt == 1:
            self.puzzle_attempt2()
            #self.get_letter()
        elif attempt == 2:
            self.puzzle_attempt3()
            #self.get_letter()
        elif attempt == 3:
            self.puzzle_attempt4()
            #self.get_letter()
        elif attempt == 4:      
            self.puzzle_attempt5()
            #self.get_letter()
        elif attempt == 5:       #I am no too sure if is "else" or "elif"
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
           
    def puzzle_attempt2(self) :
         
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
        
    def puzzle_attempt3(self) :
        
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
    
    def puzzle_attempt4(self) :
        
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
        
    
    def puzzle_attempt5(self) :
    
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

    def puzzle_attempt6(self) :
    
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

    
