"""
Game class for managing the game state and loop.
"""

import pygame

from snake_game.objects.game_board import GameBoard
from snake_game.objects.snake import Snake
from snake_game.utils import (
    DOWN,
    FPS,
    LEFT,
    RIGHT,
    UP,
)


class Game:
    """
    Manages the game state and loop.
    """

    def __init__(self):
        """
        Initialize the game.
        """
        self.board = GameBoard()
        self.snake = Snake()
        self.running = False
        self.game_over = False
        self.clock = pygame.time.Clock()
        self.score = 0

        # Initialize pygame
        pygame.init()

    def start(self):
        """
        Start the game.
        """
        self.running = True
        self.game_over = False
        self.score = 0

        # Reset the game board and snake
        self.board.clear()
        self.snake = Snake()

    def stop(self):
        """
        Stop the game.
        """
        self.running = False

    def handle_input(self):
        """
        Handle user input.

        Returns:
            bool: True if game should continue, False if it should exit
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

                # Handle direction changes
                if event.key == pygame.K_UP:
                    self.snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction(RIGHT)

                # Handle game restart
                if self.game_over and event.key == pygame.K_r:
                    self.start()

        return True

    def update(self):
        """
        Update the game state.

        Returns:
            bool: True if game should continue, False if it should exit
        """
        if not self.running or self.game_over:
            return True

        # Move the snake
        new_head = self.snake.move()

        # Check for collisions with walls
        if not self.board.is_position_valid(new_head):
            self.game_over = True
            return True

        # Check for collisions with self
        if self.snake.is_collision_with_self():
            self.game_over = True
            return True

        return True

    def run_game_loop(self):
        """
        Run the main game loop.

        Returns:
            bool: True if game should restart, False if it should exit
        """
        # Start the game
        self.start()

        # Main game loop
        while self.running:
            # Handle input
            if not self.handle_input():
                self.stop()
                return False

            # Update game state
            if not self.update():
                self.stop()
                return False

            # Control game speed
            self.clock.tick(FPS)

        return True

    def cleanup(self):
        """
        Clean up resources.
        """
        pygame.quit()
