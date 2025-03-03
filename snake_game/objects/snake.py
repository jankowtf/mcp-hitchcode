"""
Snake class for managing the snake's segments and movement.
"""

from snake_game.utils import GRID_HEIGHT, GRID_WIDTH, RIGHT, is_collision


class Snake:
    """
    Manages the snake's segments, movement, and growth/shrinkage.
    """

    def __init__(self, start_position=(5, 5), start_direction=RIGHT, start_length=3):
        """
        Initialize the snake.

        Args:
            start_position (tuple): Starting position of the snake's head (x, y)
            start_direction (tuple): Starting direction of the snake
            start_length (int): Starting length of the snake
        """
        self.direction = start_direction
        self.segments = []

        # Create initial segments
        for i in range(start_length):
            # Place segments in reverse direction from the head
            x = start_position[0] - i * start_direction[0]
            y = start_position[1] - i * start_direction[1]
            self.segments.append((x, y))

    @property
    def head(self):
        """
        Get the position of the snake's head.

        Returns:
            tuple: Position of the snake's head (x, y)
        """
        return self.segments[0]

    @property
    def length(self):
        """
        Get the length of the snake.

        Returns:
            int: Length of the snake
        """
        return len(self.segments)

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

    def change_direction(self, new_direction):
        """
        Change the snake's direction.

        Args:
            new_direction (tuple): New direction

        Returns:
            bool: True if direction was changed, False otherwise
        """
        # Prevent 180-degree turns
        if (
            new_direction[0] == -self.direction[0]
            and new_direction[1] == -self.direction[1]
        ):
            return False

        self.direction = new_direction
        return True

    def grow(self, amount=1):
        """
        Grow the snake by adding segments to its tail.

        Args:
            amount (int): Number of segments to add
        """
        for _ in range(amount):
            # Duplicate the last segment to grow the snake
            tail = self.segments[-1]
            self.segments.append(tail)

    def shrink(self, amount=1):
        """
        Shrink the snake by removing segments from its tail.

        Args:
            amount (int): Number of segments to remove

        Returns:
            int: Actual number of segments removed
        """
        # Ensure the snake doesn't shrink below a minimum length of 1
        amount = min(amount, max(0, self.length - 1))

        for _ in range(amount):
            if self.length > 1:
                self.segments.pop()

        return amount

    def is_collision_with_self(self):
        """
        Check if the snake's head collides with any of its body segments.

        Returns:
            bool: True if collision with self, False otherwise
        """
        head = self.head

        # Check collision with all segments except the head
        for segment in self.segments[1:]:
            if is_collision(head, segment):
                return True

        return False

    def is_position_occupied(self, position):
        """
        Check if a position is occupied by any part of the snake.

        Args:
            position (tuple): Position to check (x, y)

        Returns:
            bool: True if position is occupied, False otherwise
        """
        for segment in self.segments:
            if is_collision(position, segment):
                return True

        return False
