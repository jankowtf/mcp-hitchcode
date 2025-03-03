"""
Bomb class for the Snake game.
"""

import random

from snake_game.utils import GRID_HEIGHT, GRID_WIDTH, RED


class Bomb:
    """
    Represents a bomb that decreases the snake's length when hit.
    """

    def __init__(self, game_board, snake, position=None):
        """
        Initialize a bomb.

        Args:
            game_board: The game board instance
            snake: The snake instance
            position (tuple, optional): Position of the bomb (x, y). If None, a random position is generated.
        """
        self.game_board = game_board
        self.snake = snake
        self.color = RED

        if position:
            self.position = position
        else:
            self.position = self.generate_random_position()

        # Place the bomb on the game board
        self.game_board.place_object(self.position, "bomb")

    def generate_random_position(self):
        """
        Generate a random position for the bomb that doesn't collide with the snake or other objects.

        Returns:
            tuple: Random position (x, y)
        """
        while True:
            # Generate random position
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            position = (x, y)

            # Check if position is valid (not occupied by snake, fruits, or other bombs)
            if not self.snake.is_position_occupied(
                position
            ) and self.game_board.is_position_empty(position):
                return position

    def remove(self):
        """
        Remove the bomb from the game board.
        """
        self.game_board.remove_object(self.position)
