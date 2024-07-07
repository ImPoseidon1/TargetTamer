# TargetTamer

A simple yet engaging aim trainer game built with Python and Pygame. Improve your mouse accuracy and reaction time with this customizable target practice application.

## Features

- Two game modes:
  - Regular Mode: Click on targets to destroy them
  - God Mode: Click anywhere to destroy the nearest target
- Dynamic target generation and growth
- Score tracking: hits, misses, and accuracy
- Time-based gameplay
- Lives system
- End-game statistics display

## Requirements
- Python
- Pygame

## Installation

1. Ensure you have Python installed on your system.
2. Install Pygame by running:
   ```bash
   pip install pygame
   ```
3. Clone this repository or download the source code.

## How to Play

1. Run the script:
   ```bash
   python main.py
   ```
2. Select your desired game mode (Regular or God Mode).
3. Click on targets as they appear on the screen.
4. The game ends when you run out of lives (miss too many targets).
5. View your end-game statistics.

## Game Controls

- Mouse movement: Aim
- Left mouse button: Shoot/Select

## Customization

You can easily customize various aspects of the game by modifying the constants at the beginning of the script:

- `WIDTH`, `HEIGHT`: Changes the window size
- `MAX_LIVES`: Adjusts the total number of lives
- `TARGET_INCREMENT`: Modifies the frequency of target generation
- `Target.MAX_SIZE`: Changes the maximum size of targets
- `Target.GROWTH_RATE`: Adjust how quickly targets grow and shrink

   
