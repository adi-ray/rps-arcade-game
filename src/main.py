"""
Main game module for the Stone-Paper-Scissors game.
"""
import pygame
import sys
from pygame.locals import *

from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, MENU, TUTORIAL, GAME, RESULT, init_fonts
from src.assets import load_assets
from src.game_state import GameState
from src.screens.menu import draw_menu
from src.screens.tutorial import draw_tutorial
from src.screens.game import draw_game
from src.screens.result import draw_result

class Game:
    """Main game class"""
    
    def __init__(self):
        """Initialize the game"""
        # Initialize pygame
        pygame.init()
        pygame.mixer.init()
        
        # Set up the screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED)
        pygame.display.set_caption(SCREEN_TITLE)
        
        # Load fonts
        self.fonts = init_fonts()
        
        # Load assets
        self.assets, self.sounds = load_assets()
        
        # Initialize game state
        self.game_state = GameState(self.sounds)
        self.current_state = MENU
        
        # Set up the clock
        self.clock = pygame.time.Clock()
        
    def run(self):
        """Main game loop"""
        running = True
        
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.handle_mouse_click(mouse_pos)
            
            # Draw the current game state
            self.draw_current_state()
            
            # Update the display
            pygame.display.flip()
            self.clock.tick(60)
        
        # Clean up
        pygame.quit()
        sys.exit()
        
    def handle_mouse_click(self, mouse_pos):
        """Handle mouse clicks based on the current game state"""
        if self.current_state == MENU:
            start_button, tutorial_button = draw_menu(self.screen, self.fonts)
            if start_button.collidepoint(mouse_pos):
                self.current_state = GAME
            elif tutorial_button.collidepoint(mouse_pos):
                self.current_state = TUTORIAL
        
        elif self.current_state == TUTORIAL:
            back_button = draw_tutorial(self.screen, self.fonts, self.assets)
            if back_button.collidepoint(mouse_pos):
                self.current_state = MENU
        
        elif self.current_state == GAME:
            if self.game_state.player_choice is None:  # Only allow choice if player hasn't chosen yet
                stone_button, paper_button, scissors_button = draw_game(self.screen, self.fonts, self.assets, self.game_state)
                if stone_button.collidepoint(mouse_pos):
                    self.game_state.player_choice = "stone"
                elif paper_button.collidepoint(mouse_pos):
                    self.game_state.player_choice = "paper"
                elif scissors_button.collidepoint(mouse_pos):
                    self.game_state.player_choice = "scissors"
                
                if self.game_state.player_choice:  # If player made a choice
                    self.game_state.ai_choice = self.game_state.get_ai_choice()
                    self.game_state.determine_winner()
            else:  # Player has already chosen, click to continue
                self.game_state.next_round()
                
                # Check if game is over
                if self.game_state.is_game_over():
                    self.current_state = RESULT
                    if self.game_state.player_score > self.game_state.ai_score and self.sounds["victory"]:
                        self.sounds["victory"].play()
        
        elif self.current_state == RESULT:
            play_again_button, quit_button = draw_result(self.screen, self.fonts, self.game_state)
            if play_again_button.collidepoint(mouse_pos):
                self.game_state.reset()
                self.current_state = GAME
            elif quit_button.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()
    
    def draw_current_state(self):
        """Draw the current game state"""
        if self.current_state == MENU:
            draw_menu(self.screen, self.fonts)
        elif self.current_state == TUTORIAL:
            draw_tutorial(self.screen, self.fonts, self.assets)
        elif self.current_state == GAME:
            draw_game(self.screen, self.fonts, self.assets, self.game_state)
        elif self.current_state == RESULT:
            draw_result(self.screen, self.fonts, self.game_state)
