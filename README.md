## cse210-03

Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time.

## Synopsis

### Project Structure

    .
    ├── .gitignore
    ├── jumper
    │   ├── __main__.py               # The initial launch file
    │   └── game
    │       ├── data                  # directory that contains data but no scripts
    │       │   └── word_list.txt     # contains the master word list
    │       ├── __init__.py           # Contains project configuration variables
    │       ├── director.py           # Directs the game action
    │       ├── jumper.py             # #### NEEDS DESCRIPTION ####
    │       ├── puzzle.py             # #### NEEDS DESCRIPTION ####
    │       └── word_generator.py     # performs the game action
    └── README.md

## Required Technologies

- Python 3.x

## Rules

- The puzzle is a secret word randomly chosen from a list.
- The player guesses a letter in the puzzle.
- If the guess is correct, the letter is revealed.
- If the guess is incorrect, a line is cut on the player's parachute.
- If the puzzle is solved the game is over.
- If the player has no more parachute the game is over.

## Requirements

- The program must include a README file.
- The program must include class and method comments.
- The program must have at least four classes.
- The program must remain true to game play described in the overview.

## Things to do for fun

- Enhanced input validation.
- Enhanced game play and game over messages.
- Enhanced game display, e.g. parachute

## Authors

- Josh Ausborne
- Jesus Tortolero
- Felix Flores
- Kaylie Nelson
- Lilly Armenta
