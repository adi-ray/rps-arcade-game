#!/usr/bin/env python3
"""
Entry point for the Stone-Paper-Scissors game.
"""
import os
import sys

# Add the parent directory to the path so we can import the src package
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.main import Game

if __name__ == "__main__":
    # Create and run the game
    game = Game()
    game.run()
