# Snake Game

A straightforward implementation of the classic Snake game in Python using Pygame.

## Features

- Classic snake movement and controls
- Fruits that increase the snake's length when eaten
- Bombs that decrease the snake's length when hit
- Dynamic difficulty: each fruit eaten spawns a new bomb
- Bombs remain on the canvas until hit by the snake
- Wall wrap feature: snake can pass through walls and emerge from the opposite side
- Score tracking and game over conditions
- High score tracking
- Visual effects and animations
- Sound effects (can be toggled on/off)
- Detailed game statistics

## Requirements

- Python 3.8 or higher
- Pygame 2.0 or higher

## Installation

This project uses Poetry for dependency management. To install:

```bash
# Clone the repository
git clone <repository-url>
cd snake_game

# Install dependencies with Poetry
poetry install

# Run the game
poetry run python snake_game/main.py
```

If you don't have Poetry installed, you can install it following the instructions at [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation).

## How to Play

- Use arrow keys to control the snake's direction
- Eat fruits (green) to grow longer and increase your score
- Avoid bombs (red) as they will decrease your snake's length
- The snake can pass through walls and emerge from the opposite side
- Each fruit eaten will spawn a new bomb, increasing the difficulty
- The game ends when the snake's length becomes zero or when it hits itself
- Try to achieve the highest score possible!

## Controls

- **Arrow Up**: Move snake up
- **Arrow Down**: Move snake down
- **Arrow Left**: Move snake left
- **Arrow Right**: Move snake right
- **R**: Restart game after game over
- **S**: Toggle sound effects on/off
- **ESC**: Quit game

## Game Features

### Scoring System
- Each fruit eaten adds 10 points to your score
- The high score is tracked between game sessions
- Game statistics are displayed at game over

### Wall Wrap
- The snake can pass through walls and emerge from the opposite side
- This creates more strategic gameplay options
- Use this feature to quickly navigate across the game board

### Visual Effects
- Snake changes color when eating a fruit
- Snake flashes when hitting a bomb
- Fruits and bombs have pulsating animations
- Semi-transparent overlay on game over screen

### Sound Effects
- Sound when eating a fruit
- Sound when hitting a bomb
- Sound when game over
- Sounds can be toggled on/off with the S key

## Project Structure

```
snake_game/
├── pyproject.toml
├── README.md
├── snake_game/
│   ├── __init__.py
│   ├── main.py
│   ├── game.py
│   ├── utils.py
│   ├── sounds/
│   │   ├── eat.wav
│   │   ├── hit.wav
│   │   └── game_over.wav
│   └── objects/
│       ├── __init__.py
│       ├── snake.py
│       ├── fruit.py
│       ├── bomb.py
│       └── game_board.py
└── tests/
    ├── __init__.py
    └── test_game.py
``` 