"""
Test script to verify edge cases for the wall wrap functionality of the Snake game.
"""

import unittest

from snake_game.objects.bomb import Bomb
from snake_game.objects.fruit import Fruit
from snake_game.objects.game_board import GameBoard
from snake_game.objects.snake import Snake
from snake_game.utils import GRID_WIDTH, RIGHT


class TestWallWrapEdgeCases(unittest.TestCase):
    """
    Test edge cases for the wall wrap functionality.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.board = GameBoard()
        self.snake = Snake()

    def test_wrap_while_growing(self):
        """
        Test wrapping around a wall while the snake is growing.
        """
        # Position at the right edge
        position = (GRID_WIDTH - 1, 5)
        self.snake.segments = [position]
        self.snake.direction = RIGHT

        # Grow the snake
        original_length = self.snake.length
        self.snake.grow()

        # Move right (should wrap to left edge)
        new_head = self.snake.move()

        # Verify the snake wrapped correctly
        self.assertEqual(new_head[0], 0)
        self.assertEqual(new_head[1], 5)

        # Verify the snake grew
        self.assertEqual(self.snake.length, original_length + 1)

    def test_multiple_segments_crossing(self):
        """
        Test multiple segments crossing a wall at once.
        """
        # Create a snake with segments near the right edge
        self.snake.segments = [
            (GRID_WIDTH - 3, 5),
            (GRID_WIDTH - 2, 5),
            (GRID_WIDTH - 1, 5),
        ]
        self.snake.direction = RIGHT

        # Move right three times (all segments should wrap)
        for _ in range(3):
            self.snake.move()

        # Verify all segments wrapped correctly
        self.assertEqual(self.snake.segments[0][0], 0)  # Head should be at x=0
        self.assertEqual(
            self.snake.segments[1][0], GRID_WIDTH - 1
        )  # Second segment at right edge
        self.assertEqual(
            self.snake.segments[2][0], GRID_WIDTH - 2
        )  # Tail at second-to-last column

    def test_fruit_near_wall(self):
        """
        Test interaction with a fruit near a wall.
        """
        # Create a snake at the right edge
        self.snake.segments = [(GRID_WIDTH - 1, 5)]
        self.snake.direction = RIGHT

        # Create a fruit at the left edge (where the snake will wrap to)
        fruit = Fruit(self.board, self.snake, position=(0, 5))

        # Move right (should wrap to left edge and be at the fruit's position)
        new_head = self.snake.move()

        # Verify the snake wrapped correctly to the fruit's position
        self.assertEqual(new_head, fruit.position)

    def test_bomb_near_wall(self):
        """
        Test interaction with a bomb near a wall.
        """
        # Create a snake at the right edge
        self.snake.segments = [(GRID_WIDTH - 1, 5)]
        self.snake.direction = RIGHT

        # Create a bomb at the left edge (where the snake will wrap to)
        bomb = Bomb(self.board, self.snake, position=(0, 5))

        # Move right (should wrap to left edge and be at the bomb's position)
        new_head = self.snake.move()

        # Verify the snake wrapped correctly to the bomb's position
        self.assertEqual(new_head, bomb.position)


if __name__ == "__main__":
    unittest.main()
