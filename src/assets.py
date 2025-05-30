"""
Asset loading and management for the Stone-Paper-Scissors game.
"""
import os
import pygame
from src.config import NES_BLACK, NES_RED, NES_GREEN, NES_BLUE, NES_YELLOW, NES_WHITE

def create_placeholder_image(width, height, color, text=""):
    """Create a placeholder image with text"""
    surface = pygame.Surface((width, height))
    surface.fill(color)
    if text:
        font = pygame.font.Font(None, 32)
        text_surf = font.render(text, True, NES_BLACK)
        text_rect = text_surf.get_rect(center=(width/2, height/2))
        surface.blit(text_surf, text_rect)
    return surface

def load_image(filename):
    """Load an image and return a pygame surface"""
    try:
        image_path = os.path.join('assets', filename)
        if not os.path.exists(image_path):
            print(f"Image file not found: {image_path}")
            return create_placeholder_image(100, 100, NES_RED, filename)
        image = pygame.image.load(image_path)
        return image
    except pygame.error as e:
        print(f"Unable to load image: {filename} - {e}")
        return create_placeholder_image(100, 100, NES_RED, filename)

def load_sound(filename):
    """Load a sound and return a pygame sound object"""
    try:
        sound_path = os.path.join('assets', filename)
        if not os.path.exists(sound_path):
            print(f"Sound file not found: {sound_path}")
            return None
        return pygame.mixer.Sound(sound_path)
    except pygame.error as e:
        print(f"Unable to load sound: {filename} - {e}")
        return None

def load_music(filename):
    """Load and play background music"""
    try:
        music_path = os.path.join('assets', filename)
        if not os.path.exists(music_path):
            print(f"Music file not found: {music_path}")
            return False
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)  # Loop forever
        return True
    except pygame.error as e:
        print(f"Unable to load music: {filename} - {e}")
        return False

def load_assets(audio_available=True):
    """Load all game assets and return them in a dictionary"""
    # Create assets directory if it doesn't exist
    if not os.path.exists('assets'):
        os.makedirs('assets')
        
    # Placeholder assets
    assets = {
        "stone": create_placeholder_image(100, 100, NES_RED, "STONE"),
        "paper": create_placeholder_image(100, 100, NES_GREEN, "PAPER"),
        "scissors": create_placeholder_image(100, 100, NES_BLUE, "SCISSORS"),
        "stone_anim": [create_placeholder_image(100, 100, NES_RED, "STONE"), 
                      create_placeholder_image(110, 110, NES_RED, "STONE!")],
        "paper_anim": [create_placeholder_image(100, 100, NES_GREEN, "PAPER"), 
                      create_placeholder_image(110, 110, NES_GREEN, "PAPER!")],
        "scissors_anim": [create_placeholder_image(100, 100, NES_BLUE, "SCISSORS"), 
                         create_placeholder_image(110, 110, NES_BLUE, "SCISSORS!")],
        "heart": create_placeholder_image(30, 30, NES_RED, "♥"),
        "empty_heart": create_placeholder_image(30, 30, NES_BLACK, "♡"),
        "happy_face": create_placeholder_image(50, 50, NES_YELLOW, "😊"),
        "annoyed_face": create_placeholder_image(50, 50, NES_YELLOW, "😠"),
        "angry_face": create_placeholder_image(50, 50, NES_YELLOW, "💢"),
        "vs_screen": create_placeholder_image(400, 200, NES_YELLOW, "VS"),
        "start_button": create_placeholder_image(200, 80, NES_GREEN, "PRESS START"),
        "tutorial": create_placeholder_image(600, 400, NES_WHITE, "TUTORIAL: Stone > Scissors > Paper > Stone")
    }

    # Try to load actual assets if they exist
    asset_files = {
        "stone": "stone_pixel.png",
        "paper": "paper_pixel.png",
        "scissors": "scissors_pixel.png",
        "heart": "heart_pixel.png",
        "empty_heart": "empty_heart_pixel.png",
        "happy_face": "happy_face_pixel.png",
        "annoyed_face": "annoyed_face_pixel.png",
        "angry_face": "angry_face_pixel.png",
        "vs_screen": "vs_screen_pixel.png",
        "tutorial": "tutorial_pixel.png"
    }

    for key, filename in asset_files.items():
        if os.path.exists(os.path.join('assets', filename)):
            assets[key] = load_image(filename)

    # Sound effects (only if audio is available)
    sounds = {}
    if audio_available:
        sounds = {
            "rock_smash": load_sound("rock_smash.wav"),
            "paper_flip": load_sound("paper_flip.wav"),
            "scissors_snip": load_sound("scissors_snip.wav"),
            "victory": load_sound("victory_jingle.wav"),
            "critical": load_sound("critical_hit.wav")
        }
        
        # Try to load music
        load_music("main_theme.mod")
    else:
        print("Audio disabled. Game will run without sound effects and music.")
    
    return assets, sounds
