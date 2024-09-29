# intro123

Hi in this post will contains 2 file (not include this one )
1. profile (my personal profile)
2. a simple game call "Pong NOOB AI debsirin" (its just a pong game with a simple physics of bouncing ball with a NOOB Newbie AI that will keep you busy for a while)
ABOUT THE Pong game
# Pong Game

This is a simple Pong game implemented in Python using the SimpleGUI library.

## Requirements

- Python 3.x
- SimpleGUICS2Pygame library

## Installation

1. **Install Python 3.x**: If you don't have Python installed, download and install it from [python.org](https://www.python.org/).

2. **Install SimpleGUICS2Pygame**: This is a reimplementation of SimpleGUI for Python 3.

    ```sh
    pip install SimpleGUICS2Pygame
    ```

## How to Run the Game

1. **Clone the repository** (or download the `game.py` file):

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Run the game**:

    ```sh
    python game.py
    ```

## How to Play

- **Player 1 Controls**:
  - `W` key: Move paddle up
  - `S` key: Move paddle down

- **Player 2 Controls**:
  - `Up Arrow` key: Move paddle up
  - `Down Arrow` key: Move paddle down

- **Objective**: The objective of the game is to hit the ball with your paddle and make it past your opponent's paddle. The game keeps track of the score for both players.

## Code Overview

- **`keyup(key)`**: This function handles the key release events and updates the paddle velocities accordingly.
- **`toggle_mode()`**: This function toggles between single-player and multiplayer modes.

Feel free to explore the code and make modifications to enhance the game!
## What I Learned from Developing This Game

1. **Basic Game Development Concepts**:
   - **Game Loop**: Understanding how the game loop works, which continuously updates the game state and renders the game visuals.
   - **Event Handling**: Learning how to handle user inputs such as key presses and button clicks to control game elements.

2. **Python Programming Skills**:
   - **Variables and Data Types**: Using different data types such as integers, floats, and lists to manage game state.
   - **Functions**: Defining and using functions to organize code and handle specific tasks like drawing on the canvas, updating positions, and handling inputs.
   - **Global Variables**: Managing global variables to maintain the state of the game across different functions.

3. **SimpleGUI Library**:
   - **Creating a Frame**: Setting up the game window using `simplegui.create_frame`.
   - **Drawing on Canvas**: Using the draw handler to render game elements like paddles, ball, and scores.
   - **Event Handlers**: Setting up keydown and keyup handlers to respond to user inputs and control the paddles.

4. **Game Physics**:
   - **Collision Detection**: Implementing collision detection for the ball with the paddles and walls.
   - **Velocity and Position Updates**: Understanding how to update the position of game elements based on their velocity and handling boundary conditions.

5. **AI Implementation**:
   - **Basic AI**: Implementing a simple AI to control the second paddle in single-player mode, making it follow the ball.

6. **Code Organization and Modularity**:
   - **Modular Code**: Writing modular code by separating different functionalities into distinct functions, making the code easier to read and maintain.
   - **Initialization and Reset**: Implementing functions to initialize and reset the game state, such as `new_game` and `spawn_ball`.








