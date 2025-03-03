"""
Utility functions and constants for the Snake game.
"""

# Game constants
GRID_SIZE = 20  # Size of each grid cell in pixels
GRID_WIDTH = 30  # Number of grid cells in width
GRID_HEIGHT = 20  # Number of grid cells in height
SCREEN_WIDTH = GRID_WIDTH * GRID_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Game speed (frames per second)
FPS = 10


def grid_to_pixel(grid_pos):
    """
    Convert grid coordinates to pixel coordinates.

    Args:
        grid_pos (tuple): Grid coordinates (x, y)

    Returns:
        tuple: Pixel coordinates (x, y)
    """
    return (grid_pos[0] * GRID_SIZE, grid_pos[1] * GRID_SIZE)


def pixel_to_grid(pixel_pos):
    """
    Convert pixel coordinates to grid coordinates.

    Args:
        pixel_pos (tuple): Pixel coordinates (x, y)

    Returns:
        tuple: Grid coordinates (x, y)
    """
    return (pixel_pos[0] // GRID_SIZE, pixel_pos[1] // GRID_SIZE)


def is_collision(pos1, pos2):
    """
    Check if two positions collide.

    Args:
        pos1 (tuple): First position (x, y)
        pos2 (tuple): Second position (x, y)

    Returns:
        bool: True if positions collide, False otherwise
    """
    return pos1[0] == pos2[0] and pos1[1] == pos2[1]
