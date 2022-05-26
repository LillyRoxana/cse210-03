from game.puzzle import Puzzle

class Jumper:
    """The person who seeks to decipher the Puzzle. 
    
    The responsibility of a jumper/player is to keep a record of the letters 
    he/she has given and the attempts he/she has made (whether these have been correct or incorrect).
    
    Attributes:
        letter (str): The letter proposed by the jumper/player (a-z).
    """
   
    def __init__(self):
        """Constructs a new Jumper/Player
         
        Args: 
            self(Puzzle): An instance of Jumper
        """
        self._letters = []
      
    def get_letters(self, selected_word):
        """This method will print the lines of the random word
        
        Args:
            self (Player): An instance of Jumper.
            random_word (string): The random word, that the player need to guess.
        """
        number_letters = ''
        for letter in selected_word:
            if letter == ' ':
                number_letters += letter
            else:
                if letter in self._letters:
                    number_letters += letter
                else:
                    number_letters += '_'
            
            number_letters += ' '
        return (number_letters)

    def add_letter(self,new_letter, puzzle_word):
        #this method add the guess letter to a list
        if new_letter in puzzle_word:
            if new_letter not in self._letters:
                self._letters.append(new_letter)
                #print(self._letters)#It is working
            return True
        return False    



#    def add_letter(self, letter):
#        self._letter.append(letter) 
