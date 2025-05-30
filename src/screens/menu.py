"""
Menu screen for the Stone-Paper-Scissors game.
"""
import pygame
from src.config import SCREEN_WIDTH, NES_BLACK, NES_WHITE, NES_YELLOW, NES_GREEN, NES_BLUE

def draw_menu(screen, fonts):
    """Draw the main menu screen and return button rectangles"""
    screen.fill(NES_BLACK)
    title = fonts["large"].render("STONE-PAPER-SCISSORS", True, NES_WHITE)
    subtitle = fonts["medium"].render("8-BIT BATTLE", True, NES_YELLOW)
    
    screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, 150))
    screen.blit(subtitle, (SCREEN_WIDTH/2 - subtitle.get_width()/2, 220))
    
    # Draw start button
    start_button_rect = pygame.Rect(SCREEN_WIDTH/2 - 100, 350, 200, 80)
    pygame.draw.rect(screen, NES_GREEN, start_button_rect)
    start_text = fonts["medium"].render("START", True, NES_BLACK)
    screen.blit(start_text, (start_button_rect.centerx - start_text.get_width()/2, 
                            start_button_rect.centery - start_text.get_height()/2))
    
    # Draw tutorial button
    tutorial_button_rect = pygame.Rect(SCREEN_WIDTH/2 - 100, 450, 200, 80)
    pygame.draw.rect(screen, NES_BLUE, tutorial_button_rect)
    tutorial_text = fonts["medium"].render("TUTORIAL", True, NES_BLACK)
    screen.blit(tutorial_text, (tutorial_button_rect.centerx - tutorial_text.get_width()/2, 
                               tutorial_button_rect.centery - tutorial_text.get_height()/2))
    
    return start_button_rect, tutorial_button_rect
