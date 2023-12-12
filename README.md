# ROCK PAPER SCISSORS
This project is a version of the classic Rock, Paper, Scissors game designed for two players. Both players have the opportunity to choose between rock ('r'), paper ('p') or scissors ('s'). After each election, the program determines the winner based on the fundamental rules of the game.

The rules are simple:

Stone crushes scissors (Stone beats Scissors).
Scissors cut paper (Scissors beat Paper).
Paper covers stone (Paper beats Stone).

At the end of each round, the option to play again is offered. Enter 'y' to continue with another round or 'n' to end the game.

Immerse yourself in the fun of this classic decision and strategy game with a friend!

## 🎮 Try My Rock, Paper, Scissors Game! 🎮
Ready to play? Just click the link below and dive into the fun of this classic decision-making game. I hope you enjoy playing as much as I enjoyed creating it!

Play here on repl.it!
https://replit.com/@gallegosamantha/rock-paper-scisors

Have fun and feel free to leave your feedback! 😊👾

#Coding #GameDev #Python #InteractiveFun

## Code Walkthrough: Unveiling the Logic Behind the Game
To understand a little more how this code works, I am going to explain it to you step by step.

### Step 1: Import the getpass Function from the getpass Library
First we  import the getpass function from the getpass library, to ensure that whenever you use input, each player cannot see what the other player typed in 😉:

```python
from getpass import getpass as input
```
### Step 2: Introduce the Game and Get Player 1's Input
A message is printed to indicate that the game is about to start, and Player 1 is asked to choose their move (rock, paper, or scissors). A while loop is used to ensure that the player's input is valid, and an error message is displayed if it's not.
```python
print("It's time to start this battle, select your move (s, r, or p)")
while True:
    while True:    
        player_1 = input("Player 1: ")
        if player_1.lower() != 's' and player_1.lower() != 'r' and player_1.lower() != 'p':
            print("Not valid, please select your move (s, r, or p)")
        else:
            break
```
### Step 3: Get Player 2's Input
Similar to the previous step, Player 2 is asked to choose their move, and the validity of the input is checked using a while loop.
```python
while True:
    player_2 = input("Player 2: ")
    if player_2.lower() != 's' and player_2.lower() != 'r' and \
       player_2.lower() != 'p':
        print("Not valid, please select your move (s, r, or p)")
    else:
        break
```
### Step 4: Determine the Winner and Display the Result
The possible combinations of moves are evaluated to determine the winner. A message is displayed indicating whether Player 1, Player 2, or both players tie.

```python
if (player_1.lower() == 'r' and player_2.lower() == 's') or \
   (player_1.lower() == 's' and player_2.lower() == 'p') or \
   (player_1.lower() == 'p' and player_2.lower() == 'r'):
    print("¡Player 1 wins!")
elif (player_2.lower() == 'r' and player_1.lower() == 's') or \
     (player_2.lower() == 's' and player_1.lower() == 'p') or \
     (player_2.lower() == 'p' and player_1.lower() == 'r'):
    print("¡Player 2 wins!")
else:
    print("It's a tie")
```
### Step 5: Ask if They Want to Play Again
Players are asked if they want to play again. If the answer is not 'y' (yes), the main loop is exited, ending the game.
```python
pa = input("Do you want to play again? (y/n): ")
if pa.lower() != 'y':
    break
```
## Additional Notes:
* The code uses input from the getpass module to hide the players' input.
* A main loop (while True) is implemented to allow for multiple rounds of the game.
* Comparisons are performed in lowercase (player_1.lower()), allowing players to enter 'S', 'R', or 'P' in any combination of uppercase and lowercase.
