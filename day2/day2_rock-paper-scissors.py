#!/usr/bin/env python3

"""--- Day 2: Rock Paper Scissors ---
The Elves begin to set up camp on the beach. To decide whose tent gets to be closest
to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds;
in each round, the players each simultaneously choose one of Rock, Paper, or 
Scissors using a hand shape. Then, a winner for that round is selected:
Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. 
If both players choose the same shape, the round instead ends in a draw.
an encrypted strategy guide (your puzzle input) that they say will be sure to help you win.
 
The first column is what your opponent is going to play: 
    - A for Rock, B for Paper, and C for Scissors.
The second column, you reason, must be what you should play in response:
    -  X for Rock, Y for Paper, and Z for Scissors.

The winner of the whole tournament is the player with the highest score. 
Your total score is the sum of your scores for each round.
The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper,
and 3 for Scissors) plus the score for the outcome of the round
 (0 if you lost, 3 if the round was a draw, and 6 if you won).

For example, suppose you were given the following strategy guide:

A Y
B X
C Z
...

This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). 
This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). 
This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

All possibilits:
draw | Y: 3, win | Z:6, loss | X:0
r A|X: 1, p B|Y:2, s C|Z:3

A vs X : draw (3+1=4)(0+2=3) A vs Y : win  (6+2=8)(3+1=4)  A vs Z : loss (0+3=3)(6+2=8)
B vs X : loss (0+1=1)(0+3=1) B vs Y : draw (3+2=5)(3+2=5)  B vs Z : win  (6+3=9)(6+3=9)
C vs X : win  (6+1=7)(0+2=2) C vs Y : loss (0+2=2)(3+3=6)  C vs Z : draw (3+3=6)(6+1=7)
"""

import os

file = 'input_day2.txt'
FILEPATH = os.path.join(os.curdir,file)

score = {
    'A X': 4, 'A Y': 8, 'A Z': 3,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 7, 'C Y': 2, 'C Z': 6,
    }

score_2p = {
    'A X': 3, 'A Y': 4, 'A Z': 8,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 2, 'C Y': 6, 'C Z': 7,
    }


total_score=0
total_score_2p=0

with open(FILEPATH) as file:
    rounds = [i for i in file.read().strip().split('\n') ]
   # print(rounds)

for round in rounds:
    total_score += score[round]

    total_score_2p += score_2p[round]
    
print(total_score)
print(total_score_2p)




