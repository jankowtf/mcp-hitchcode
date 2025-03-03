"""
Game class for managing the game state and loop.
"""

import os

import pygame
import pygame.font
import pygame.mixer

from snake_game.objects.bomb import Bomb
from snake_game.objects.fruit import Fruit
from snake_game.objects.game_board import GameBoard
from snake_game.objects.snake import Snake
from snake_game.utils import (
    ANIMATION_FRAMES,
    BLACK,
    BLUE,
    DOWN,
    FLASH_FRAMES,
    FPS,
    FRUIT_SCORE,
    GRAY,
    GREEN,
    GRID_SIZE,
    LEFT,
    LIGHT_BLUE,
    LIGHT_GREEN,
    PURPLE,
    RED,
    RIGHT,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SOUND_ENABLED,
    UP,
    WHITE,
    YELLOW,
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
        self.high_score = 0
        self.fruit = None
        self.bombs = []

        # Animation variables
        self.animation_counter = 0
        self.flash_counter = 0
        self.fruit_eaten = False
        self.bomb_hit = False

        # Game statistics
        self.fruits_eaten = 0
        self.bombs_hit = 0
        self.max_snake_length = 3

        # Initialize pygame
        pygame.init()

        # Initialize sound if enabled
        if SOUND_ENABLED:
            pygame.mixer.init()
            self.load_sounds()

        # Set up the display
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")

        # Set up fonts for UI
        self.font = pygame.font.SysFont("Arial", 24)
        self.large_font = pygame.font.SysFont("Arial", 48)
        self.small_font = pygame.font.SysFont("Arial", 18)

    def load_sounds(self):
        """
        Load sound effects.
        """
        self.sounds = {}

        # Create sounds directory if it doesn't exist
        sounds_dir = os.path.join(os.path.dirname(__file__), "sounds")
        os.makedirs(sounds_dir, exist_ok=True)

        # Define sound file paths
        sound_files = {
            "eat": os.path.join(sounds_dir, "eat.wav"),
            "hit": os.path.join(sounds_dir, "hit.wav"),
            "game_over": os.path.join(sounds_dir, "game_over.wav"),
        }

        # Try to load sounds, but don't crash if files don't exist
        for name, path in sound_files.items():
            try:
                if os.path.exists(path):
                    self.sounds[name] = pygame.mixer.Sound(path)
                else:
                    # Create placeholder sounds with different frequencies
                    buffer = pygame.mixer.Sound(buffer=bytes(256))
                    self.sounds[name] = buffer
            except:
                # If sound loading fails, create a silent sound
                self.sounds[name] = pygame.mixer.Sound(buffer=bytes(256))

    def start(self):
        """
        Start the game.
        """
        self.running = True
        self.game_over = False
        self.score = 0

        # Reset animation variables
        self.animation_counter = 0
        self.flash_counter = 0
        self.fruit_eaten = False
        self.bomb_hit = False

        # Reset game statistics
        self.fruits_eaten = 0
        self.bombs_hit = 0
        self.max_snake_length = 3

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

                # Toggle sound
                if event.key == pygame.K_s:
                    global SOUND_ENABLED
                    SOUND_ENABLED = not SOUND_ENABLED

        return True

    def update(self):
        """
        Update the game state.

        Returns:
            bool: True if game should continue, False if it should exit
        """
        if not self.running or self.game_over:
            return True

        # Update animation counters
        if self.fruit_eaten:
            self.animation_counter += 1
            if self.animation_counter >= ANIMATION_FRAMES:
                self.animation_counter = 0
                self.fruit_eaten = False

        if self.bomb_hit:
            self.flash_counter += 1
            if self.flash_counter >= FLASH_FRAMES:
                self.flash_counter = 0
                self.bomb_hit = False

        # Move the snake
        new_head = self.snake.move()

        # Check for collisions with walls
        if not self.board.is_position_valid(new_head):
            self.game_over_sequence()
            return True

        # Check for collisions with self
        if self.snake.is_collision_with_self():
            self.game_over_sequence()
            return True

        # Check for collision with fruit
        if self.fruit and new_head == self.fruit.position:
            # Increase score
            self.score += FRUIT_SCORE

            # Update high score
            if self.score > self.high_score:
                self.high_score = self.score

            # Update statistics
            self.fruits_eaten += 1

            # Set animation flag
            self.fruit_eaten = True
            self.animation_counter = 0

            # Play sound
            if SOUND_ENABLED and "eat" in self.sounds:
                self.sounds["eat"].play()

            # Grow the snake
            self.snake.grow()

            # Update max snake length
            if self.snake.length > self.max_snake_length:
                self.max_snake_length = self.snake.length

            # Respawn the fruit
            self.fruit.respawn()

            # Add a new bomb
            self.bombs.append(Bomb(self.board, self.snake))

        # Check for collision with bombs
        bombs_to_remove = []
        for bomb in self.bombs:
            if new_head == bomb.position:
                # Set animation flag
                self.bomb_hit = True
                self.flash_counter = 0

                # Update statistics
                self.bombs_hit += 1

                # Play sound
                if SOUND_ENABLED and "hit" in self.sounds:
                    self.sounds["hit"].play()

                # Shrink the snake
                self.snake.shrink()

                # Remove the bomb
                bomb.remove()
                bombs_to_remove.append(bomb)

                # Check if snake length is zero
                if self.snake.length == 0:
                    self.game_over_sequence()
                    return True

        # Remove hit bombs from the list
        for bomb in bombs_to_remove:
            self.bombs.remove(bomb)

        return True

    def game_over_sequence(self):
        """
        Handle game over sequence.
        """
        self.game_over = True

        # Play game over sound
        if SOUND_ENABLED and "game_over" in self.sounds:
            self.sounds["game_over"].play()

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
            if i == 0:  # Head
                color = LIGHT_GREEN if self.fruit_eaten else GREEN
            else:  # Body
                color = LIGHT_BLUE if self.fruit_eaten else BLUE

            # Flash red if bomb was hit
            if self.bomb_hit and self.flash_counter % 2 == 0:
                color = RED

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

            # Use pulsating effect for fruit
            color = self.fruit.color
            if self.animation_counter % 2 == 0:
                color = YELLOW

            # Draw the fruit
            pygame.draw.rect(
                self.screen,
                color,
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

            # Use pulsating effect for bombs
            color = bomb.color
            if self.animation_counter % 2 == 0:
                color = PURPLE

            # Draw the bomb
            pygame.draw.rect(
                self.screen,
                color,
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

        # Draw high score
        high_score_text = self.font.render(
            f"High Score: {self.high_score}", True, YELLOW
        )
        self.screen.blit(high_score_text, (10, 40))

        # Draw length
        length_text = self.font.render(f"Length: {self.snake.length}", True, WHITE)
        self.screen.blit(length_text, (10, 70))

        # Draw sound status
        sound_status = "ON" if SOUND_ENABLED else "OFF"
        sound_text = self.small_font.render(
            f"Sound: {sound_status} (S to toggle)", True, WHITE
        )
        self.screen.blit(sound_text, (SCREEN_WIDTH - 200, 10))

        # Draw game over message if game is over
        if self.game_over:
            # Semi-transparent overlay
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 128))  # Black with alpha
            self.screen.blit(overlay, (0, 0))

            # Game over text
            game_over_text = self.large_font.render("GAME OVER", True, RED)
            restart_text = self.font.render("Press R to restart", True, WHITE)

            # Statistics
            stats_text = [
                f"Final Score: {self.score}",
                f"High Score: {self.high_score}",
                f"Fruits Eaten: {self.fruits_eaten}",
                f"Bombs Hit: {self.bombs_hit}",
                f"Max Snake Length: {self.max_snake_length}",
            ]

            # Center the game over text
            game_over_rect = game_over_text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80)
            )
            restart_rect = restart_text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40)
            )

            # Draw the text
            self.screen.blit(game_over_text, game_over_rect)
            self.screen.blit(restart_text, restart_rect)

            # Draw statistics
            for i, stat in enumerate(stats_text):
                stat_text = self.font.render(stat, True, WHITE)
                stat_rect = stat_text.get_rect(
                    center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20 + i * 30)
                )
                self.screen.blit(stat_text, stat_rect)

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
