"""
Fruit class for the Snake game.
"""

import random

from snake_game.utils import GREEN, GRID_HEIGHT, GRID_WIDTH


class Fruit:
    """
    Represents a fruit that increases the snake's length when eaten.
    """

    def __init__(self, game_board, snake, position=None):
        """
        Initialize a fruit.

        Args:
            game_board: The game board instance
            snake: The snake instance
            position (tuple, optional): Position of the fruit (x, y). If None, a random position is generated.
        """
        self.game_board = game_board
        self.snake = snake
        self.color = GREEN

        if position:
            self.position = position
        else:
            self.position = self.generate_random_position()

        # Place the fruit on the game board
        self.game_board.place_object(self.position, "fruit")

    def generate_random_position(self):
        """
        Generate a random position for the fruit that doesn't collide with the snake or other objects.

        Returns:
            tuple: Random position (x, y)
        """
        while True:
            # Generate random position
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            position = (x, y)

            # Check if position is valid (not occupied by snake or other objects)
            if not self.snake.is_position_occupied(
                position
            ) and self.game_board.is_position_empty(position):
                return position

    def respawn(self):
        """
        Respawn the fruit at a new random position.
        """
        # Remove the fruit from its current position
        self.game_board.remove_object(self.position)

        # Generate a new position
        self.position = self.generate_random_position()

        # Place the fruit at the new position
        self.game_board.place_object(self.position, "fruit")
