#!/usr/bin/env python3

""" the Elves begin taking inventory of their supplies. One important 
consideration is food - in particular, the number of Calories each
Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained 
by the various meals, snacks, rations, etc. that they've brought with them,one 
item per line. Each Elf separates  their own inventory from the previous Elf's 
inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end up
 with the following list:

1000
2000
3000

4000

5000
6000

...

This list represents the Calories of the food carried by five Elves:

The first Elf is carrying food with 1000, 2000, and 3000 Calories,
a total of 6000 Calories.The second Elf is carrying one food item 
with 4000 Calories.The third Elf is carrying food with 5000 and 
6000 Calories, a total of 11000 Calories.

In case the Elves get hungry and need extra snacks, they need 
to know which Elf to ask: they'd like to know how many Calories 
are being carried by the Elf carrying the most Calories. 
In the example above, this is 11000 (carried by the third Elf).
 
Find the Elf carrying the most Calories. How many total Calories is 
that Elf carrying?
"""

__version_ = "0.1.0"
__author__ = "Regina Celi da Silva"

import os
import sys

input_file = 'input(d1)_Calorie _Counting.txt'
FILEPATH = os.path.join(os.curdir, input_file)

count=0
num=0

lista=[]
for line in open(FILEPATH):
    data = line.strip().split("\n\n")

    for i in data:
        if i == "":
           count = 0
        else:
            num = int(i)
            count += num

        lista.append(count)
                          
print(max(lista), len(lista))
print(sorted(lista)[-3:])
print(sum([66773, 67997, 74711]))