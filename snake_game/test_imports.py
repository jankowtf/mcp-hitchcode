"""
Test script to verify imports work correctly.
"""

try:
    from snake_game.game import Game
    from snake_game.objects.bomb import Bomb
    from snake_game.objects.fruit import Fruit
    from snake_game.objects.game_board import GameBoard
    from snake_game.objects.snake import Snake
    from snake_game.utils import GRID_HEIGHT, GRID_WIDTH

    print("All imports successful!")
    print("Game:", Game)
    print("Snake:", Snake)
    print("Fruit:", Fruit)
    print("Bomb:", Bomb)
    print("GameBoard:", GameBoard)
    print("GRID_WIDTH:", GRID_WIDTH)
    print("GRID_HEIGHT:", GRID_HEIGHT)
except ImportError as e:
    print(f"Import error: {e}")
