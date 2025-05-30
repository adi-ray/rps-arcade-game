# Stone-Paper-Scissors: 8-Bit Battle

A retro-style Stone-Paper-Scissors game with pixel art graphics and 8-bit music, built with PyGame.

## Repository

GitHub: https://github.com/adi-ray/rps-arcade-game

## Features

- Classic Stone-Paper-Scissors gameplay with a retro arcade twist
- Pixel art graphics with authentic NES color palette
- 8-bit music and sound effects
- Dynamic AI opponent that adapts to your gameplay
- Special "Critical Hit" system with a 5% chance to deal double damage
- AI "Rage Quit" mode when player wins 3 times in a row
- Health bar system with pixel hearts
- AI mood meter that changes based on game progress

## Code Structure

The game follows a modular architecture for better organization and maintainability:

```
stone_paper_scissors_game/
├── assets/                  # Game assets directory
├── src/                     # Source code directory
│   ├── __init__.py          # Makes src a Python package
│   ├── assets.py            # Asset loading functions
│   ├── config.py            # Game configuration and constants
│   ├── game_state.py        # Game state management
│   ├── main.py              # Main game class
│   ├── screens/             # Different game screens
│   │   ├── __init__.py
│   │   ├── game.py          # Main game screen
│   │   ├── menu.py          # Menu screen
│   │   ├── result.py        # Result screen
│   │   └── tutorial.py      # Tutorial screen
│   └── utils/               # Utility functions
│       ├── __init__.py
│       └── helpers.py       # Helper functions
├── run_game.py              # Script to run the game
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/adi-ray/rps-arcade-game.git
cd rps-arcade-game
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
python run_game.py
```

## Controls

- Use your mouse to navigate menus and make choices
- Click on Stone, Paper, or Scissors to make your move
- Click anywhere to continue after each round

## Asset Requirements

The game looks for the following assets in an `assets` folder:

### Images
- `stone_pixel.png` - Rock with crack effects
- `paper_pixel.png` - Folded origami style
- `scissors_pixel.png` - Glowing blades
- `heart_pixel.png` - Pixel heart for health display
- `empty_heart_pixel.png` - Empty heart outline
- `happy_face_pixel.png` - AI happy mood
- `annoyed_face_pixel.png` - AI annoyed mood
- `angry_face_pixel.png` - AI angry mood
- `vs_screen_pixel.png` - VS screen animation
- `tutorial_pixel.png` - Tutorial screen graphic

### Sounds
- `rock_smash.wav` - Sound effect for stone
- `paper_flip.wav` - Sound effect for paper
- `scissors_snip.wav` - Sound effect for scissors
- `victory_jingle.wav` - Victory sound
- `critical_hit.wav` - Critical hit sound effect
- `main_theme.mod` - Background music (8-bit chiptune)

If these assets are not found, the game will use placeholder graphics and no sound.

## Creating Pixel Art Assets

For the best retro look, create your pixel art assets using the NES color palette:

- Black: (0, 0, 0)
- White: (255, 255, 255)
- Red: (188, 56, 56)
- Green: (88, 176, 60)
- Blue: (48, 80, 184)
- Yellow: (248, 216, 96)
- Orange: (236, 88, 0)
- Brown: (168, 92, 28)
- Purple: (144, 48, 136)
- Cyan: (0, 168, 168)
- Pink: (252, 116, 180)
- Gray: (104, 104, 104)

Recommended tools for creating pixel art:
- Aseprite
- PyxelEdit
- Piskel (free, browser-based)

## Creating 8-bit Music

Recommended tools for creating 8-bit music:
- FamiTracker (authentic NES sound)
- Bosca Ceoil (beginner-friendly)
- BeepBox (browser-based)
- LMMS (with chiptune plugins)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by classic arcade games and the NES era
- Built with PyGame

## Asset Requirements

The game looks for the following assets in an `assets` folder:

### Images
- `stone_pixel.png` - Rock with crack effects
- `paper_pixel.png` - Folded origami style
- `scissors_pixel.png` - Glowing blades
- `heart_pixel.png` - Pixel heart for health display
- `empty_heart_pixel.png` - Empty heart outline
- `happy_face_pixel.png` - AI happy mood
- `annoyed_face_pixel.png` - AI annoyed mood
- `angry_face_pixel.png` - AI angry mood
- `vs_screen_pixel.png` - VS screen animation
- `tutorial_pixel.png` - Tutorial screen graphic

### Sounds
- `rock_smash.wav` - Sound effect for stone
- `paper_flip.wav` - Sound effect for paper
- `scissors_snip.wav` - Sound effect for scissors
- `victory_jingle.wav` - Victory sound
- `critical_hit.wav` - Critical hit sound effect
- `main_theme.mod` - Background music (8-bit chiptune)

If these assets are not found, the game will use placeholder graphics and no sound.

## Creating Pixel Art Assets

For the best retro look, create your pixel art assets using the NES color palette:

- Black: (0, 0, 0)
- White: (255, 255, 255)
- Red: (188, 56, 56)
- Green: (88, 176, 60)
- Blue: (48, 80, 184)
- Yellow: (248, 216, 96)
- Orange: (236, 88, 0)
- Brown: (168, 92, 28)
- Purple: (144, 48, 136)
- Cyan: (0, 168, 168)
- Pink: (252, 116, 180)
- Gray: (104, 104, 104)

Recommended tools for creating pixel art:
- Aseprite
- PyxelEdit
- Piskel (free, browser-based)

## Creating 8-bit Music

Recommended tools for creating 8-bit music:
- FamiTracker (authentic NES sound)
- Bosca Ceoil (beginner-friendly)
- BeepBox (browser-based)
- LMMS (with chiptune plugins)

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch: `git checkout -b new-feature`
3. Make your changes
4. Commit your changes: `git commit -m 'Add new feature'`
5. Push to the branch: `git push origin new-feature`
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by classic arcade games and the NES era
- Built with PyGame
