"""
Configuration settings for the Stone-Paper-Scissors game.
"""
import pygame

# Screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Stone-Paper-Scissors: 8-Bit Battle"

# Game states
MENU = 0
TUTORIAL = 1
GAME = 2
RESULT = 3

# Game settings
MAX_ROUNDS = 5
CRITICAL_HIT_CHANCE = 0.05  # 5% chance for critical hit

# NES Palette
NES_BLACK = (0, 0, 0)
NES_WHITE = (255, 255, 255)
NES_RED = (188, 56, 56)
NES_GREEN = (88, 176, 60)
NES_BLUE = (48, 80, 184)
NES_YELLOW = (248, 216, 96)
NES_ORANGE = (236, 88, 0)
NES_BROWN = (168, 92, 28)
NES_PURPLE = (144, 48, 136)
NES_CYAN = (0, 168, 168)
NES_PINK = (252, 116, 180)
NES_GRAY = (104, 104, 104)

# Font setup
def init_fonts():
    """Initialize and return game fonts"""
    return {
        "small": pygame.font.Font(None, 32),
        "medium": pygame.font.Font(None, 48),
        "large": pygame.font.Font(None, 72)
    }
