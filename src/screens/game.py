"""
Main game screen for the Stone-Paper-Scissors game.
"""
import pygame
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, NES_BLACK, NES_WHITE, NES_GREEN, NES_RED, NES_YELLOW

def draw_game(screen, fonts, assets, game_state):
    """Draw the game screen and return button rectangles"""
    screen.fill(NES_BLACK)
    
    # Draw round info
    round_text = fonts["medium"].render(f"Round {game_state.round_num}/{game_state.max_rounds}", True, NES_WHITE)
    screen.blit(round_text, (SCREEN_WIDTH/2 - round_text.get_width()/2, 20))
    
    # Draw score/health
    for i in range(game_state.max_rounds):
        if i < game_state.player_score:
            screen.blit(assets["heart"], (20 + i*40, 20))
        else:
            screen.blit(assets["empty_heart"], (20 + i*40, 20))
            
        if i < game_state.ai_score:
            screen.blit(assets["heart"], (SCREEN_WIDTH - 50 - i*40, 20))
        else:
            screen.blit(assets["empty_heart"], (SCREEN_WIDTH - 50 - i*40, 20))
    
    # Draw AI mood
    if game_state.ai_mood == "happy":
        screen.blit(assets["happy_face"], (SCREEN_WIDTH - 70, 70))
    elif game_state.ai_mood == "annoyed":
        screen.blit(assets["annoyed_face"], (SCREEN_WIDTH - 70, 70))
    else:  # angry
        screen.blit(assets["angry_face"], (SCREEN_WIDTH - 70, 70))
    
    # Draw player and AI labels
    player_label = fonts["small"].render("PLAYER", True, NES_GREEN)
    ai_label = fonts["small"].render("AI", True, NES_RED)
    screen.blit(player_label, (100 - player_label.get_width()/2, 70))
    screen.blit(ai_label, (SCREEN_WIDTH - 100 - ai_label.get_width()/2, 130))
    
    # Draw choices
    if game_state.player_choice:
        screen.blit(assets[game_state.player_choice], (100 - 50, 150))
    
    if game_state.ai_choice:
        screen.blit(assets[game_state.ai_choice], (SCREEN_WIDTH - 100 - 50, 150))
    
    # Draw result
    if game_state.result:
        if game_state.result == "win":
            result_text = fonts["medium"].render("YOU WIN!", True, NES_GREEN)
        elif game_state.result == "lose":
            result_text = fonts["medium"].render("YOU LOSE!", True, NES_RED)
        else:
            result_text = fonts["medium"].render("DRAW!", True, NES_YELLOW)
        screen.blit(result_text, (SCREEN_WIDTH/2 - result_text.get_width()/2, 150))
    
    # Draw choice buttons
    stone_button_rect = pygame.Rect(SCREEN_WIDTH/2 - 175, 350, 100, 100)
    paper_button_rect = pygame.Rect(SCREEN_WIDTH/2 - 50, 350, 100, 100)
    scissors_button_rect = pygame.Rect(SCREEN_WIDTH/2 + 75, 350, 100, 100)
    
    screen.blit(assets["stone"], stone_button_rect)
    screen.blit(assets["paper"], paper_button_rect)
    screen.blit(assets["scissors"], scissors_button_rect)
    
    # Draw button labels
    stone_label = fonts["small"].render("STONE", True, NES_WHITE)
    paper_label = fonts["small"].render("PAPER", True, NES_WHITE)
    scissors_label = fonts["small"].render("SCISSORS", True, NES_WHITE)
    
    screen.blit(stone_label, (stone_button_rect.centerx - stone_label.get_width()/2, 
                             stone_button_rect.bottom + 10))
    screen.blit(paper_label, (paper_button_rect.centerx - paper_label.get_width()/2, 
                             paper_button_rect.bottom + 10))
    screen.blit(scissors_label, (scissors_button_rect.centerx - scissors_label.get_width()/2, 
                               scissors_button_rect.bottom + 10))
    
    return stone_button_rect, paper_button_rect, scissors_button_rect
