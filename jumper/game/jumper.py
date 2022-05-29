
class Jumper:
    """The person looking for the Jumper . 
    
    The responsibility of the jumper is to add new items to a list of Jumper
    
    Attributes:
    letter (Jumper): The game's Jumper.
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._letters = []
        

    def add_letter(self, letter):
        self._letters.append(letter.lower())
