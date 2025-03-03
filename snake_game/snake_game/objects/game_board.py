"""
GameBoard class for managing the game area.
"""

from snake_game.utils import GRID_HEIGHT, GRID_WIDTH


class GameBoard:
    """
    Manages the game area and placement of objects.
    """

    def __init__(self):
        """
        Initialize the game board.
        """
        self.width = GRID_WIDTH
        self.height = GRID_HEIGHT
        self.grid = [[None for _ in range(self.height)] for _ in range(self.width)]

    def is_position_valid(self, position):
        """
        Check if a position is within the game board boundaries.

        Args:
            position (tuple): Position to check (x, y)

        Returns:
            bool: True if position is valid, False otherwise
        """
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    def is_position_empty(self, position):
        """
        Check if a position is empty (not occupied by any object).

        Args:
            position (tuple): Position to check (x, y)

        Returns:
            bool: True if position is empty, False otherwise
        """
        x, y = position
        if not self.is_position_valid(position):
            return False
        return self.grid[x][y] is None

    def place_object(self, position, obj_type):
        """
        Place an object on the game board.

        Args:
            position (tuple): Position to place the object (x, y)
            obj_type (str): Type of object to place

        Returns:
            bool: True if object was placed successfully, False otherwise
        """
        x, y = position
        if not self.is_position_valid(position):
            return False

        self.grid[x][y] = obj_type
        return True

    def remove_object(self, position):
        """
        Remove an object from the game board.

        Args:
            position (tuple): Position to remove the object from (x, y)

        Returns:
            str or None: Type of object removed, or None if no object was removed
        """
        x, y = position
        if not self.is_position_valid(position):
            return None

        obj_type = self.grid[x][y]
        self.grid[x][y] = None
        return obj_type

    def get_object_at(self, position):
        """
        Get the object at a position.

        Args:
            position (tuple): Position to check (x, y)

        Returns:
            str or None: Type of object at the position, or None if no object
        """
        x, y = position
        if not self.is_position_valid(position):
            return None

        return self.grid[x][y]

    def clear(self):
        """
        Clear the game board.
        """
        self.grid = [[None for _ in range(self.height)] for _ in range(self.width)]

    def is_collision_with_object(self, position, obj_type):
        """
        Check if a position collides with an object of a specific type.

        Args:
            position (tuple): Position to check (x, y)
            obj_type (str): Type of object to check for

        Returns:
            bool: True if position collides with an object of the specified type, False otherwise
        """
        x, y = position
        if not self.is_position_valid(position):
            return False

        return self.grid[x][y] == obj_type
