#!/usr/bin/ven python3

"""--- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded from the ships.
Supplies are stored in stacks of marked crates, but because the needed supplies are buried 
under many other crates, the crates need to be rearranged.
To ensure none of the crates get crushed or fall over, the crane operator will rearrange them 
in a series of carefully-planned steps. After the crates are rearranged, the desired crates 
will be at the top of each stack.

They do, have a drawing of the starting stacks of crates and the rearrangement procedure 
(your puzzle input). For example:
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
 
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

In this example, there are three stacks of crates. 
Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. 
Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. 
Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, 
a quantity of crates is moved from one stack to a different stack. 
In the first step of the above rearrangement procedure, one crate is 
moved from stack 2 to stack 1, resulting in this configuration:
[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
In the second step, three crates are moved from stack 1 to stack 3. 
Crates are moved one at  a time, so the first crate to be moved (D) 
ends up below the second and third crates:
        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved 
one at a time, crate C ends up below crate M:
        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
Finally, one crate is moved from stack 1 to stack 2:
        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
The Elves just need to know which crate will end up on top of each stack; 
in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, 
so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?


"""

__version__ = "0.1.0"
__author__ = "Regina Celi da Silva"

import os

file_="input_day5.txt"


def c_matriz(l,c, valor):
    matriz=[]
    for i in range(l):
        l=[]
        for j in range(c):
            l.append(valor)
        matriz.append(l)
           
    return matriz


A = c_matriz(3,2,0)
A[1][1]=2

print(A)