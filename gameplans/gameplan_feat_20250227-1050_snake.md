# Game Plan: Snake Game Implementation

## Project Overview
Create a classic Snake game in Python with the following special features:
- Bombs that appear each time the snake eats a fruit and remain in place
- Super fruits that add 3 elements to the snake at once
- Super fruits appear and disappear randomly with a 5-second delay

## Technology Stack
- Python
- Pygame for graphics and game loop
- uv for dependency management

## Implementation Stages

### Stage 1: Project Setup & Structure
- [ ] Create project directory structure
- [ ] Set up dependency management with uv
- [ ] Install required packages (pygame)
- [ ] Create basic file structure (main.py, game.py, snake.py, food.py, bomb.py)

**Implementation Details:**
- Use a modular approach with separate classes for Snake, Food, Bomb, and Game
- Set up a virtual environment using uv
- Create a main entry point that initializes the game

### Stage 2: Basic Game Elements
- [ ] Implement Snake class with movement and growth functionality
- [ ] Implement regular Food class
- [ ] Implement SuperFood class with appearance/disappearance timing
- [ ] Implement Bomb class
- [ ] Create grid-based game board

**Implementation Details:**
- Snake will be represented as a list of coordinates
- Food will be randomly placed on the grid
- SuperFood will have a timer for appearance/disappearance
- Bombs will be stored in a list and rendered on the grid
- Use a grid system for positioning all elements

### Stage 3: Game Logic
- [ ] Implement snake movement mechanics
- [ ] Implement collision detection (walls, self, food, bombs)
- [ ] Implement food consumption and snake growth
- [ ] Implement bomb generation after food consumption
- [ ] Implement super food mechanics (random appearance, timer, extra growth)

**Implementation Details:**
- Snake moves in the current direction by adding a new head and removing the tail
- When food is consumed, the tail is not removed (snake grows)
- When super food is consumed, add 3 segments to the snake
- Check for collisions with bombs, walls, and self to trigger game over
- Super food appears randomly and disappears after 5 seconds

### Stage 4: Rendering & Display
- [ ] Set up Pygame window and display
- [ ] Implement rendering of the snake
- [ ] Implement rendering of regular food
- [ ] Implement rendering of super food with distinct appearance
- [ ] Implement rendering of bombs
- [ ] Add game grid/background

**Implementation Details:**
- Use different colors for different game elements
- Snake: green
- Regular food: red
- Super food: gold/yellow with pulsing effect
- Bombs: black/dark gray
- Add visual indicators for super food timer

### Stage 5: User Input & Controls
- [ ] Implement keyboard controls for snake direction
- [ ] Add input handling for game start/restart
- [ ] Implement pause functionality
- [ ] Add game speed control (optional)

**Implementation Details:**
- Use arrow keys for direction control
- Prevent 180-degree turns (can't immediately go in the opposite direction)
- Space bar for pause/resume
- Enter/Return for restart after game over

### Stage 6: Game Loop & Timing
- [ ] Implement main game loop
- [ ] Add timing for snake movement speed
- [ ] Implement super food appearance/disappearance timer
- [ ] Add difficulty progression (optional: snake speeds up as it grows)

**Implementation Details:**
- Use Pygame's clock functionality to control game speed
- Implement a timer for super food that counts down from 5 seconds
- Random chance for super food to appear when no super food is present

### Stage 7: Scoring & Game States
- [ ] Implement scoring system
- [ ] Add game over condition
- [ ] Create start screen
- [ ] Create game over screen with final score
- [ ] Implement game restart functionality

**Implementation Details:**
- Score increases with each food item consumed
- Super food gives 3x the points of regular food
- Game over when snake collides with wall, itself, or a bomb
- Display high score from previous games

### Stage 8: Polish & Refinements
- [ ] Add sound effects for movement, eating, and collisions
- [ ] Improve visuals with better sprites/graphics
- [ ] Add animations for snake movement and growth
- [ ] Implement difficulty levels
- [ ] Add optional grid lines for better visibility
- [ ] Create a settings menu

**Implementation Details:**
- Use simple sound effects for key game events
- Add smooth animations for snake movement
- Implement a settings menu for adjusting game speed, sound volume, etc.
- Add visual effects when consuming super food or colliding with bombs

## Testing Plan
- [ ] Test snake movement in all directions
- [ ] Test collision detection with all game elements
- [ ] Test food and bomb placement logic
- [ ] Test super food timer functionality
- [ ] Test scoring system
- [ ] Test game restart functionality
- [ ] Perform playtesting for game balance and difficulty

## Deliverables
- Complete Python Snake game with all specified features
- README with game instructions and controls
- Requirements file for dependencies
- Documentation of code structure and game mechanics 