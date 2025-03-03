#!/usr/bin/env python3
"""
Main entry point for the Snake game.
"""

import sys

from snake_game.game import Game


def main():
    """
    Main function to initialize and run the game.
    """
    # Create and run the game
    game = Game()

    try:
        # Run the game loop
        restart = game.run_game_loop()

        # If the game should restart, do so
        while restart:
            restart = game.run_game_loop()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Clean up resources
        game.cleanup()
        sys.exit()


if __name__ == "__main__":
    main()
