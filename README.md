# 🎮 8-Bit Stone-Paper-Scissors Battle

A retro arcade-style Rock-Paper-Scissors experience with authentic pixel art and chiptune music, built with PyGame.

<div align="center">
  <!-- Tech Stack -->
  <a href="https://pygame.org">
    <img src="https://custom-icon-badges.demolab.com/badge/Powered_By-Pygame_2.5+-ff6600?logo=pygame&style=for-the-badge&logoColor=white" alt="Pygame">
  </a>
  <a href="https://www.python.org/downloads/">
    <img src="https://custom-icon-badges.demolab.com/badge/Python-3.8%2B-3776ab?logo=python&style=for-the-badge" alt="Python">
  </a>
  <a href="https://aws.amazon.com/q/">
    <img src="https://custom-icon-badges.demolab.com/badge/Assisted_By-Amazon_Q-FF9900?logo=amazonaws&style=for-the-badge" alt="Amazon Q">
  </a>
</div>

<div align="center">
  <!-- Community -->
  <a href="CONTRIBUTING.md">
    <img src="https://custom-icon-badges.demolab.com/badge/Contributions-Welcome-2ecc71?logo=git-pull-request&style=for-the-badge" alt="Contributions">
  </a>
  <a href="https://github.com/adi-ray/rps-arcade-game/blob/main/LICENSE">
    <img src="https://custom-icon-badges.demolab.com/badge/License-MIT-3498db?logo=law&style=for-the-badge" alt="MIT License">
  </a>
  <a href="https://dev.to/adiray">
    <img src="https://custom-icon-badges.demolab.com/badge/Dev_Blog-Post-0A0A0A?logo=dev.to&style=for-the-badge" alt="Dev Blog">
  </a>
</div>

## ✨ Features

- Classic Stone-Paper-Scissors gameplay with a retro arcade twist
- Pixel art graphics with authentic NES color palette
- 8-bit music and sound effects
- Dynamic AI opponent that adapts to your gameplay
- Special "Critical Hit" system with a 5% chance to deal double damage
- AI "Rage Quit" mode when player wins 3 times in a row
- Health bar system with pixel hearts
- AI mood meter that changes based on game progress

## 🛠️ Installation

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

> **Note**: Requires Python 3.8+ and PyGame 2.0+

## 🕹️ Controls

- Use your mouse to navigate menus and make choices
- Click on Stone, Paper, or Scissors to make your move
- Click anywhere to continue after each round

## 🗂️ Project Structure

The game follows a modular architecture for better organization and maintainability:

```plaintext
stone_paper_scissors_game/
├── assets/              # All game assets (images/sounds)
├── src/
│   ├── screens/         # Game state screens
│   │   ├── game.py      # Core gameplay
│   │   ├── menu.py      # Main menu
│   │   └── ...
│   └── utils/           # Helper functions
├── config.py            # Game constants
└── run_game.py          # Launch script
```

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

## 🎨 Asset Creation Guide

### Recommended Tools

| Asset Type  | Tools                       |
| ----------- | --------------------------- |
| Pixel Art   | Aseprite, Piskel, PyxelEdit |
| 8-bit Music | FamiTracker, Bosca Ceoil    |

### NES Color Palette

```python
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
```

## 🤝 Contributing

Please read our [CONTRIBUTING](CONTRIBUTING.md) file for guidelines on how to get started.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

> Built with ❤️ and Amazon Q CLI 🤖  
> Inspired by classic NES arcade games 👾
