"""
Game class for managing the game state and loop.
"""

import pygame
import pygame.font

from snake_game.objects.bomb import Bomb
from snake_game.objects.fruit import Fruit
from snake_game.objects.game_board import GameBoard
from snake_game.objects.snake import Snake
from snake_game.utils import (
    BLACK,
    BLUE,
    DOWN,
    FPS,
    GRAY,
    GREEN,
    GRID_SIZE,
    LEFT,
    RED,
    RIGHT,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    UP,
    WHITE,
    grid_to_pixel,
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
        self.fruit = None
        self.bombs = []

        # Initialize pygame
        pygame.init()

        # Set up the display
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")

        # Set up fonts for UI
        self.font = pygame.font.SysFont("Arial", 24)
        self.large_font = pygame.font.SysFont("Arial", 48)

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

        # Create initial fruit
        self.fruit = Fruit(self.board, self.snake)

        # Clear bombs
        self.bombs = []

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

        # Check for collision with fruit
        if self.fruit and new_head == self.fruit.position:
            # Increase score
            self.score += 10

            # Grow the snake
            self.snake.grow()

            # Respawn the fruit
            self.fruit.respawn()

            # Add a new bomb
            self.bombs.append(Bomb(self.board, self.snake))

        # Check for collision with bombs
        bombs_to_remove = []
        for bomb in self.bombs:
            if new_head == bomb.position:
                # Shrink the snake
                self.snake.shrink()

                # Remove the bomb
                bomb.remove()
                bombs_to_remove.append(bomb)

                # Check if snake length is zero
                if self.snake.length == 0:
                    self.game_over = True
                    return True

        # Remove hit bombs from the list
        for bomb in bombs_to_remove:
            self.bombs.remove(bomb)

        return True

    def render(self):
        """
        Render the game.
        """
        # Clear the screen
        self.screen.fill(BLACK)

        # Draw the game board
        self.draw_board()

        # Draw the fruit
        self.draw_fruit()

        # Draw the bombs
        self.draw_bombs()

        # Draw the snake
        self.draw_snake()

        # Draw UI elements
        self.draw_ui()

        # Update the display
        pygame.display.flip()

    def draw_board(self):
        """
        Draw the game board.
        """
        # Draw grid lines
        for x in range(0, self.board.width + 1):
            pygame.draw.line(
                self.screen, GRAY, (x * GRID_SIZE, 0), (x * GRID_SIZE, SCREEN_HEIGHT), 1
            )

        for y in range(0, self.board.height + 1):
            pygame.draw.line(
                self.screen, GRAY, (0, y * GRID_SIZE), (SCREEN_WIDTH, y * GRID_SIZE), 1
            )

        # Draw game boundaries
        pygame.draw.rect(self.screen, WHITE, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 2)

    def draw_snake(self):
        """
        Draw the snake.
        """
        # Draw each segment of the snake
        for i, segment in enumerate(self.snake.segments):
            # Head is green, body is a slightly different shade
            color = GREEN if i == 0 else BLUE

            # Convert grid position to pixel position
            pixel_pos = grid_to_pixel(segment)

            # Draw the segment
            pygame.draw.rect(
                self.screen, color, (pixel_pos[0], pixel_pos[1], GRID_SIZE, GRID_SIZE)
            )

            # Draw a border around the segment
            pygame.draw.rect(
                self.screen,
                BLACK,
                (pixel_pos[0], pixel_pos[1], GRID_SIZE, GRID_SIZE),
                1,
            )

    def draw_fruit(self):
        """
        Draw the fruit.
        """
        if self.fruit:
            # Convert grid position to pixel position
            pixel_pos = grid_to_pixel(self.fruit.position)

            # Draw the fruit
            pygame.draw.rect(
                self.screen,
                self.fruit.color,
                (pixel_pos[0], pixel_pos[1], GRID_SIZE, GRID_SIZE),
            )

            # Draw a border around the fruit
            pygame.draw.rect(
                self.screen,
                BLACK,
                (pixel_pos[0], pixel_pos[1], GRID_SIZE, GRID_SIZE),
                1,
            )

    def draw_bombs(self):
        """
        Draw the bombs.
        """
        for bomb in self.bombs:
            # Convert grid position to pixel position
            pixel_pos = grid_to_pixel(bomb.position)

            # Draw the bomb
            pygame.draw.rect(
                self.screen,
                bomb.color,
                (pixel_pos[0], pixel_pos[1], GRID_SIZE, GRID_SIZE),
            )

            # Draw a border around the bomb
            pygame.draw.rect(
                self.screen,
                BLACK,
                (pixel_pos[0], pixel_pos[1], GRID_SIZE, GRID_SIZE),
                1,
            )

    def draw_ui(self):
        """
        Draw UI elements.
        """
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        # Draw length
        length_text = self.font.render(f"Length: {self.snake.length}", True, WHITE)
        self.screen.blit(length_text, (10, 40))

        # Draw game over message if game is over
        if self.game_over:
            game_over_text = self.large_font.render("GAME OVER", True, RED)
            restart_text = self.font.render("Press R to restart", True, WHITE)

            # Center the text
            game_over_rect = game_over_text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20)
            )
            restart_rect = restart_text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20)
            )

            # Draw the text
            self.screen.blit(game_over_text, game_over_rect)
            self.screen.blit(restart_text, restart_rect)

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

            # Render the game
            self.render()

            # Control game speed
            self.clock.tick(FPS)

        return True

    def cleanup(self):
        """
        Clean up resources.
        """
        pygame.quit()
