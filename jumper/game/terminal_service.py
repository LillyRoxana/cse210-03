class Terminal_service:

    # TODO 
    # make the methods/functions actually do stuff
    def read_letter(self,prompt):
        """Gets alphabetical input from the terminal. Directs the user with the given prompt.

                Args: 
                    self (TerminalService): An instance of TerminalService.
                    prompt (string): The prompt to display on the terminal.

                Returns:
                    a string: The user's input as a letter.
                """
        return input(prompt)

