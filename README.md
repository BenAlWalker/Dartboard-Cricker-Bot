Dartboard-Cricket-Bot

This was a project worked on during the UVA 2022 HooHacks Competition. The computer bot plays the dart game cricket against a specified number of users and uses a command line program to track the current scores of the game.

At the end of the game, there is a to-scale dartboard which displays all of the throws that the computer made during the game.

Running crick_game.py will start a game of Cricket against the bot. In order, to specify throws that the user created you can type the value of the number hit (i.e, 1-20, or 25 for bullseye). If a double 15 is hit this can be specified by typing "15 2".

When the game is over, it will show all of the shots the computer made in its attempts to play against the player.

The darts.py file - while separate from the bot - shows how the dart board was created. In this file, you can prompt the computer with an amount of darts to fire at the board, and how precise the computer will be dependent on the variance of the normal-distribution based shots.
