"""
Result screen for the Stone-Paper-Scissors game.
"""
import pygame
from src.config import SCREEN_WIDTH, NES_BLACK, NES_WHITE, NES_GREEN, NES_RED

def draw_result(screen, fonts, game_state):
    """Draw the final result screen and return button rectangles"""
    screen.fill(NES_BLACK)
    
    if game_state.player_score > game_state.ai_score:
        result_text = fonts["large"].render("YOU WIN!", True, NES_GREEN)
    else:
        result_text = fonts["large"].render("YOU LOSE!", True, NES_RED)
    
    screen.blit(result_text, (SCREEN_WIDTH/2 - result_text.get_width()/2, 200))
    
    score_text = fonts["medium"].render(f"Final Score: {game_state.player_score} - {game_state.ai_score}", True, NES_WHITE)
    screen.blit(score_text, (SCREEN_WIDTH/2 - score_text.get_width()/2, 300))
    
    # Draw play again button
    play_again_rect = pygame.Rect(SCREEN_WIDTH/2 - 150, 400, 300, 80)
    pygame.draw.rect(screen, NES_GREEN, play_again_rect)
    play_again_text = fonts["medium"].render("PLAY AGAIN", True, NES_BLACK)
    screen.blit(play_again_text, (play_again_rect.centerx - play_again_text.get_width()/2, 
                                 play_again_rect.centery - play_again_text.get_height()/2))
    
    # Draw quit button
    quit_rect = pygame.Rect(SCREEN_WIDTH/2 - 100, 500, 200, 60)
    pygame.draw.rect(screen, NES_RED, quit_rect)
    quit_text = fonts["medium"].render("QUIT", True, NES_BLACK)
    screen.blit(quit_text, (quit_rect.centerx - quit_text.get_width()/2, 
                           quit_rect.centery - quit_text.get_height()/2))
    
    return play_again_rect, quit_rect
