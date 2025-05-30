"""
Game state management for the Stone-Paper-Scissors game.
"""
import random
from src.config import MAX_ROUNDS, CRITICAL_HIT_CHANCE

class GameState:
    """Class to manage the game state"""
    
    def __init__(self, sounds):
        """Initialize the game state"""
        self.player_score = 0
        self.ai_score = 0
        self.round_num = 1
        self.max_rounds = MAX_ROUNDS
        self.player_choice = None
        self.ai_choice = None
        self.result = None
        self.ai_mood = "happy"  # Can be "happy", "annoyed", "angry"
        self.ai_consecutive_losses = 0
        self.sounds = sounds
        
    def reset(self):
        """Reset the game state for a new game"""
        self.player_score = 0
        self.ai_score = 0
        self.round_num = 1
        self.player_choice = None
        self.ai_choice = None
        self.result = None
        self.ai_mood = "happy"
        self.ai_consecutive_losses = 0
        
    def get_ai_choice(self):
        """Get AI choice based on mood and strategy"""
        # If AI is angry (player won 3 times in a row), AI picks randomly
        if self.ai_consecutive_losses >= 3:
            return random.choice(["stone", "paper", "scissors"])
        
        # Otherwise, AI tries to be smart
        if self.player_choice == "stone":
            return "paper"  # AI counters with paper
        elif self.player_choice == "paper":
            return "scissors"  # AI counters with scissors
        elif self.player_choice == "scissors":
            return "stone"  # AI counters with stone
        else:
            return random.choice(["stone", "paper", "scissors"])
            
    def determine_winner(self):
        """Determine the winner and update scores"""
        player = self.player_choice
        ai = self.ai_choice
        
        # Check for critical hit (5% chance)
        critical_hit = random.random() < CRITICAL_HIT_CHANCE
        
        if player == ai:
            self.result = "draw"
        elif (player == "stone" and ai == "scissors") or \
             (player == "paper" and ai == "stone") or \
             (player == "scissors" and ai == "paper"):
            self.result = "win"
            self.player_score += 2 if critical_hit else 1
            self.ai_consecutive_losses += 1
            
            # Update AI mood based on consecutive losses
            if self.ai_consecutive_losses >= 3:
                self.ai_mood = "angry"
            elif self.ai_consecutive_losses >= 1:
                self.ai_mood = "annoyed"
                
            # Play sound effects
            if self.sounds["critical"] and critical_hit:
                self.sounds["critical"].play()
            elif player == "stone" and self.sounds["rock_smash"]:
                self.sounds["rock_smash"].play()
            elif player == "paper" and self.sounds["paper_flip"]:
                self.sounds["paper_flip"].play()
            elif player == "scissors" and self.sounds["scissors_snip"]:
                self.sounds["scissors_snip"].play()
        else:
            self.result = "lose"
            self.ai_score += 1
            self.ai_consecutive_losses = 0
            self.ai_mood = "happy"
            
            # Play sound effects
            if ai == "stone" and self.sounds["rock_smash"]:
                self.sounds["rock_smash"].play()
            elif ai == "paper" and self.sounds["paper_flip"]:
                self.sounds["paper_flip"].play()
            elif ai == "scissors" and self.sounds["scissors_snip"]:
                self.sounds["scissors_snip"].play()
                
    def next_round(self):
        """Advance to the next round"""
        self.player_choice = None
        self.ai_choice = None
        self.result = None
        self.round_num += 1
        
    def is_game_over(self):
        """Check if the game is over"""
        return self.round_num > self.max_rounds or self.player_score >= 3 or self.ai_score >= 3
