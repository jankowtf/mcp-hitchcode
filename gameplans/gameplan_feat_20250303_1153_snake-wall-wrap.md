# Game Plan: Snake Game Wall Wrap Feature

## Overview
This game plan outlines the implementation of a wall wrap feature for the existing Snake game. This enhancement will allow the snake to pass through walls and emerge from the opposite side, rather than ending the game when hitting a wall. This creates a more forgiving gameplay experience while maintaining the core challenge of avoiding self-collisions and managing bombs.

## Current State Analysis
The existing Snake game has the following components:
1. A Snake class that manages the snake's movement, growth, and collision detection
2. A GameBoard class that manages the game area and object placement
3. A Game class that handles the game loop, input, and rendering
4. Fruit and Bomb classes for collectible and obstacle objects
5. A scoring system, visual effects, and sound effects

Currently, when the snake hits a wall, the game ends. We need to modify this behavior to implement the wall wrap feature.

## Architecture Modifications
The implementation will require changes to the following components:

1. **Game Class**: Update the collision detection logic to handle wall transitions instead of game over
2. **Snake Class**: Modify the movement logic to support wrapping around the game board
3. **GameBoard Class**: Ensure proper handling of objects at the boundaries

No changes to the overall architecture are needed, as we're enhancing existing functionality rather than adding new components.

## Implementation Stages

### Stage 1: Analysis and Planning
Tasks:
- [x] Review the existing collision detection logic in the Game class
- [x] Identify the specific code sections that handle wall collisions
- [x] Analyze the Snake class movement implementation
- [x] Determine the best approach for implementing the wrap-around logic
- [x] Create a test plan to verify the new feature works correctly

Acceptance Criteria:
- All code sections that need modification are identified
- The implementation approach is clearly defined
- Potential edge cases and issues are documented

### Stage 2: Implementation
Tasks:
- [x] Modify the Game.update() method to handle wall transitions
- [x] Update the Snake.move() method to implement wrap-around logic
- [x] Adjust the GameBoard.is_position_valid() method to accommodate the new boundary behavior
- [x] Update any relevant UI elements or messages related to wall collisions
- [x] Ensure compatibility with existing game mechanics (fruits, bombs, scoring)

Acceptance Criteria:
- Snake successfully passes through walls and emerges from the opposite side
- All existing game mechanics continue to function correctly
- No new bugs or issues are introduced

### ✅ Stage 3: Testing and Refinement
Tasks:
- [x] Test the snake's movement through all four walls (top, right, bottom, left)
- [x] Verify that fruits and bombs near walls work correctly
- [x] Test edge cases (e.g., snake wrapping while growing, multiple segments crossing at once)
- [x] Optimize the implementation if needed
- [x] Update documentation to reflect the new feature

Acceptance Criteria:
- The snake correctly wraps around all four walls
- Fruits and bombs interact properly with the snake at boundaries
- All edge cases are handled correctly
- The game runs smoothly with the new feature
- Documentation is updated to reflect the changes

## Implementation Details

### Wall Wrap Logic
When the snake reaches a wall, instead of triggering game over, we'll adjust its position to the opposite side of the game board:
- If the snake hits the right wall (x = GRID_WIDTH), it will emerge from the left wall (x = 0)
- If the snake hits the left wall (x = -1), it will emerge from the right wall (x = GRID_WIDTH - 1)
- If the snake hits the bottom wall (y = GRID_HEIGHT), it will emerge from the top wall (y = 0)
- If the snake hits the top wall (y = -1), it will emerge from the bottom wall (y = GRID_HEIGHT - 1)

### Code Modifications

#### Game Class
In the Game.update() method, we need to modify the wall collision check at line ~210:
```python
# Check for collisions with walls
if not self.board.is_position_valid(new_head):
    self.game_over_sequence()
    return True
```

This check has been removed since the snake.move() method now handles wrapping the snake around the game board boundaries.

#### Snake Class
We've modified the Snake.move() method at line ~51 to implement the wrap-around logic when the snake reaches a boundary:
```python
def move(self):
    """
    Move the snake in its current direction.

    Returns:
        tuple: New position of the snake's head
    """
    # Calculate new head position
    head_x, head_y = self.head
    dir_x, dir_y = self.direction
    new_head = (head_x + dir_x, head_y + dir_y)
    
    # Wrap the head position around the game board
    new_head = self.wrap_position(new_head)

    # Insert new head at the beginning of the segments list
    self.segments.insert(0, new_head)

    # Remove the last segment (tail)
    self.segments.pop()

    return new_head
```

We've also added a new wrap_position method to handle the wrapping logic:
```python
def wrap_position(self, position):
    """
    Wrap a position around the game board boundaries.

    Args:
        position (tuple): Position to wrap (x, y)

    Returns:
        tuple: Wrapped position (x, y)
    """
    x, y = position
    
    # Wrap horizontally
    if x >= GRID_WIDTH:
        x = 0
    elif x < 0:
        x = GRID_WIDTH - 1
        
    # Wrap vertically
    if y >= GRID_HEIGHT:
        y = 0
    elif y < 0:
        y = GRID_HEIGHT - 1
        
    return (x, y)
```

#### GameBoard Class
We've added a wrap_position method to the GameBoard class to handle wrapping positions around the game board:
```python
def wrap_position(self, position):
    """
    Wrap a position around the game board boundaries.

    Args:
        position (tuple): Position to wrap (x, y)

    Returns:
        tuple: Wrapped position (x, y)
    """
    x, y = position
    
    # Wrap horizontally
    if x >= self.width:
        x = 0
    elif x < 0:
        x = self.width - 1
        
    # Wrap vertically
    if y >= self.height:
        y = 0
    elif y < 0:
        y = self.height - 1
        
    return (x, y)
```

The Fruit and Bomb classes don't need to be modified since they already use the GameBoard's methods for position validation.

## Reasoning
The wall wrap feature is a common variation in Snake games that adds a different dimension to the gameplay. Instead of having to avoid walls, the player can use them strategically to reach fruits or avoid bombs. This creates a more forgiving experience while maintaining the core challenge of avoiding self-collisions.

The implementation approach focuses on minimal changes to the existing codebase, ensuring that all current functionality continues to work correctly while adding the new feature.

## Impact Analysis
- **Gameplay**: The game becomes more forgiving as wall collisions no longer end the game, but the challenge of avoiding self-collisions and bombs remains.
- **Difficulty**: Slightly reduced difficulty as one failure condition is removed, but this is balanced by the increased strategic options.
- **User Experience**: Players gain more freedom of movement and can develop new strategies using the wrap-around feature.
- **Code Complexity**: Minimal increase in complexity, as the changes are focused on specific areas of the codebase.

## Success Criteria
The implementation will be considered successful when:
1. The snake can pass through all four walls and emerge from the opposite side
2. All existing game mechanics (fruits, bombs, scoring, etc.) work correctly with the new feature
3. The game runs smoothly with no new bugs or issues
4. The user experience is enhanced by the added strategic options 