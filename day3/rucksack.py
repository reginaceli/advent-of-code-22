#!/usr/bin/env python3

"""--- Day 3: Rucksack Reorganization ---
One Elf has the important job of loading all of the rucksacks with supplies 
for the jungle journey. Unfortunately, that Elf didn't quite follow 
the packing instructions, and so a few items now need to be rearranged.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input),
but they need your help finding the errors. Every item type is identified by a single lowercase
or uppercase letter (that is, a and A refer to different types of items).

The list of items for each rucksack is given as characters all on a single line. 
A given rucksack always has the same number of items in each of its two compartments, 
so the first half of the characters represent items in the first compartment, while the 
second half of the characters represent items in the second compartment.

For example, suppose you have the following list of contents from six rucksacks:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
...
- The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first 
compartment contains the items vJrwpWtwJgWr, while the second compartment contains 
the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
- The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. 
The only item type that appears in both compartments is uppercase L.
- The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; 
the only common item type is uppercase P.

To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
In the above example, the priority of the item type that appears in both compartments
of each rucksack is 16 (p), 38 (L), 42 (P); the sum of these is 96.

Find the item type that appears in both compartments of each rucksack. 
What is the sum of the priorities of those item types?

--- Part Two ---
For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group. 
For efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves. 
That is, if a group's badge is item type B, then all three Elves will have item type B somewhere in their rucksack,
 and at most two of the Elves will be carrying any other item type.

The problem is that someone forgot to put this year's updated authenticity sticker on the badges. 
All of the badges need to be pulled out of the rucksacks so the new authenticity stickers can be attached.
Additionally, nobody wrote down which item type corresponds to each group's badges. 
The only way to tell which item type is the right one is by finding the one item type that is common between 
all three Elves in each group.

Every set of three lines in your list corresponds to a single group, but each group 
can have a different badge item type. So, in the above example, the first group's 
rucksacks are the first three lines:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg

And the second group's rucksacks are the next three lines:

wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw

In the first group, the only item type that appears in all three rucksacks is lowercase r; 
this must be their badges. In the second group, their badge item type must be Z.

Priorities for these items must still be found to organize the sticker attachment efforts: 
here, they are 18 (r) for the first group and 52 (Z) for the second group. The sum of these is 70.

Find the item type that corresponds to the badges of each three-Elf group. 
What is the sum of the priorities of those item types?
""" 

__version__ = '0.1.0'
__author__  = 'Regina Celi da Silva'

import os
import string

file_= 'input_day3.txt'
FILEPATH = os.path.join(os.curdir,file_)
letters = string.ascii_letters

with open(FILEPATH) as file:
    data = [i for i in file.read().strip().split('\n')]

priorities = 0
for item in data:
    print(item)
    first = set(item[:len(item)//2])
    second = set(item[len(item)//2:])
    intersection = first & second

    for priority, char in enumerate(letters, start=1):
        if char in intersection:
            priorities += priority
    print(priorities)

   
# --- Part Two ---

j=3
priorities_2p = 0

for i in range(0, len(data), 3):
    rucksacks = (data[i:j])
    intersection_2p = set(rucksacks[0]) & set(rucksacks[1]) & set(rucksacks[2])
    j += 3
    
    for priority, char in enumerate(letters, start=1):
        if char in intersection_2p:
            priorities_2p += priority
print(priorities_2p)