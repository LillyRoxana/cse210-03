## cse210-03

Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time.

## Synopsis

### Project Structure

    .
    ├── .gitignore
    ├── jumper
    │   ├── __main__.py               # The initial launch file
    │   └── game
    │       ├── director.py           # Directs the game action
    │       ├── jumper.py             # Directs the game action
    │       ├── list_words.py         # Directs the game action
    │       ├── parachute.py          # Directs the game action
    │       ├── puzzle.py             # Directs the game action
    │       └── terminal_service.py   # performs the game action
    └── README.md

## Required Technologies

- Python 3.10.0

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
