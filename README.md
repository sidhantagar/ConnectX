# ConnectX

This project in reinforcement learning has been inspired from the game of connect4 and is an extension to the Kaggle project of [ConnectX](https://github.com/sidhantagar/Kaggle-ConnectX). The game of connect4 consists of a 2D grid of 6 rows and 7 columns. In the game each of the two players take turns dropping a piece of their color in a column of their choice. The objective of the game is to connect 4 in a row horizontally vertically or diagonally. The game ends if either player achieves the objective or the board is full such that the player cannot make a move.

In the project the dimensions of the game board can be varied from 0-20 along each dimension thus creating more diverse and varied strategy profiles.Also we can change the target of the game from connecting 4 in a row to n (between 3-10.) This makes it impossible to use a predetermied stratedy such as one that exists for the conventional 6x7 board size in the connect 4 game. Thus I decided to use a heuristic  

The game has 3 different modes of Player vs Player, Player vs AI and AI vs AI.

## About the AI agent:

- The algorithm used in the agent is Minimax.
- The Minimax tree is further deepend using Dynamic Programming as the agent uses a 2 step lookahead.
- Useless branches of pruned using alpha-beta pruning in order to save precious computation time.
- For a complete description of the agent, check out my [jupyter notebook](https://github.com/sidhantagar/Kaggle-ConnectX/blob/master/Simple%20Minimax%20Agent/Agent-Explanation.ipynb) where I have uploaded a detailed explanation of the same. Or you can also fork the [notebook on Kaggle](https://www.kaggle.com/sidagar/getting-1000-score-using-only-minimax) if you want to play aroung with the code for yourself.

## About the UI interface:

- The UI interface has been developed in pygame.

## How to run the game:

1. Install python(Preferably python3) on your PC.

2. Use pip to install numpy pandas and pygame libraries.

3. Download and extract all the files in this repository.

4. Run Main_Menu.py

P.S: Running the game for the first time may take pygame considerably more time to load the interface.
