from game import Puzzle

Class Jumper:
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
    
      self._letter = []
      
    def add_letter(self, letter):
        
      self._letter.append(letter.lower()) 
