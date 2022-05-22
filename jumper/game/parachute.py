class Parachute:
   
    
   def __init__(self):
      

      self._parachutes = 0
      self._parachute = 0


   def show_parachute(self, tries):

        levels = [ 
            """
             x 
            /|\ 
            / \ 
       ^^^^^^^^^^^^^
            """,
            
            """
            \ /
             O
            /|\ 
            / \ 
       ^^^^^^^^^^^^^
            """,
         
            """
           \   /
            \ /
             O
            /|\ 
            / \ 
       ^^^^^^^^^^^^^
            """,
            
            """
          \     /
           \   /
            \ /
             O
            /|\ 
            / \ 
       ^^^^^^^^^^^^^
            """,
           
            """
          /_____\ 
          \     /
           \   /
            \ /
             O
            /|\ 
            / \ 
       ^^^^^^^^^^^^^
            """,
            
            """
           _____
          /_____\ 
          \     /
           \   /
            \ /
             O
            /|\ 
            / \ 
       ^^^^^^^^^^^^^
            """,
            ]
        
        return print(levels[tries])




