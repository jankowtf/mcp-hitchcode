"""
Test script to verify the wall wrap functionality of the Snake game.
"""

import unittest

from snake_game.objects.game_board import GameBoard
from snake_game.objects.snake import Snake
from snake_game.utils import DOWN, GRID_HEIGHT, GRID_WIDTH, LEFT, RIGHT, UP


class TestWallWrap(unittest.TestCase):
    """
    Test cases for the wall wrap functionality.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.board = GameBoard()
        self.snake = Snake()

    def test_wrap_position_right_wall(self):
        """
        Test wrapping around the right wall.
        """
        # Position at the right edge
        position = (GRID_WIDTH - 1, 5)
        self.snake.segments = [position]
        self.snake.direction = RIGHT

        # Move right (should wrap to left edge)
        new_head = self.snake.move()
        self.assertEqual(new_head[0], 0)
        self.assertEqual(new_head[1], 5)

    def test_wrap_position_left_wall(self):
        """
        Test wrapping around the left wall.
        """
        # Position at the left edge
        position = (0, 5)
        self.snake.segments = [position]
        self.snake.direction = LEFT

        # Move left (should wrap to right edge)
        new_head = self.snake.move()
        self.assertEqual(new_head[0], GRID_WIDTH - 1)
        self.assertEqual(new_head[1], 5)

    def test_wrap_position_bottom_wall(self):
        """
        Test wrapping around the bottom wall.
        """
        # Position at the bottom edge
        position = (5, GRID_HEIGHT - 1)
        self.snake.segments = [position]
        self.snake.direction = DOWN

        # Move down (should wrap to top edge)
        new_head = self.snake.move()
        self.assertEqual(new_head[0], 5)
        self.assertEqual(new_head[1], 0)

    def test_wrap_position_top_wall(self):
        """
        Test wrapping around the top wall.
        """
        # Position at the top edge
        position = (5, 0)
        self.snake.segments = [position]
        self.snake.direction = UP

        # Move up (should wrap to bottom edge)
        new_head = self.snake.move()
        self.assertEqual(new_head[0], 5)
        self.assertEqual(new_head[1], GRID_HEIGHT - 1)

    def test_gameboard_wrap_position(self):
        """
        Test the GameBoard's wrap_position method.
        """
        # Test wrapping right wall
        position = (GRID_WIDTH, 5)
        wrapped = self.board.wrap_position(position)
        self.assertEqual(wrapped, (0, 5))

        # Test wrapping left wall
        position = (-1, 5)
        wrapped = self.board.wrap_position(position)
        self.assertEqual(wrapped, (GRID_WIDTH - 1, 5))

        # Test wrapping bottom wall
        position = (5, GRID_HEIGHT)
        wrapped = self.board.wrap_position(position)
        self.assertEqual(wrapped, (5, 0))

        # Test wrapping top wall
        position = (5, -1)
        wrapped = self.board.wrap_position(position)
        self.assertEqual(wrapped, (5, GRID_HEIGHT - 1))


if __name__ == "__main__":
    unittest.main()
