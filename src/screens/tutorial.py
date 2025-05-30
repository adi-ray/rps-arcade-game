"""
Tutorial screen for the Stone-Paper-Scissors game.
"""
import pygame
from src.config import SCREEN_WIDTH, NES_BLACK, NES_WHITE, NES_YELLOW, NES_RED

def draw_tutorial(screen, fonts, assets):
    """Draw the tutorial screen and return the back button rectangle"""
    screen.fill(NES_BLACK)
    
    # Draw tutorial content
    screen.blit(assets["tutorial"], (SCREEN_WIDTH/2 - 300, 100))
    
    # Draw back button
    back_button_rect = pygame.Rect(SCREEN_WIDTH/2 - 100, 520, 200, 60)
    pygame.draw.rect(screen, NES_RED, back_button_rect)
    back_text = fonts["medium"].render("BACK", True, NES_BLACK)
    screen.blit(back_text, (back_button_rect.centerx - back_text.get_width()/2, 
                           back_button_rect.centery - back_text.get_height()/2))
    
    # Draw tutorial text
    rules1 = fonts["small"].render("Stone crushes Scissors", True, NES_WHITE)
    rules2 = fonts["small"].render("Scissors cuts Paper", True, NES_WHITE)
    rules3 = fonts["small"].render("Paper covers Stone", True, NES_WHITE)
    rules4 = fonts["small"].render("Best of 5 Rounds Wins!", True, NES_YELLOW)
    rules5 = fonts["small"].render("5% chance for Critical Hit (2x damage)!", True, NES_RED)
    
    screen.blit(rules1, (SCREEN_WIDTH/2 - rules1.get_width()/2, 320))
    screen.blit(rules2, (SCREEN_WIDTH/2 - rules2.get_width()/2, 360))
    screen.blit(rules3, (SCREEN_WIDTH/2 - rules3.get_width()/2, 400))
    screen.blit(rules4, (SCREEN_WIDTH/2 - rules4.get_width()/2, 440))
    screen.blit(rules5, (SCREEN_WIDTH/2 - rules5.get_width()/2, 480))
    
    return back_button_rect
