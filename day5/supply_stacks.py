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

--- Part Two ---
As you watch the crane operator expertly rearrange the crates, you notice the process isn't 
following your prediction. Some mud was covering the writing on the side of the crane, and
you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats,
an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
Moving a single crate from stack 2 to stack 1 behaves the same as before:
[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
However, the action of moving three crates from stack 1 to stack 3 means that those
three moved crates stay in the same order, resulting in this new configuration:
        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.
Before the rearrangement process finishes, update your simulation so that the 
Elves know where they should stand to be ready to unload the final supplies. 
After the rearrangement procedure completes, what crate ends up on top of each stack?
"""
__version__ = "0.1.0"
__author__ = "Regina Celi da Silva"

import os

file_= "input_day5.txt"
FILEPATH = os.path.join(os.curdir, file_)

with open(FILEPATH) as file:
    #s, i = (i.splitlines() for i in file.read().strip('\n').split('\n\n'))
    stack_file,instruction_file  = file.read().strip('\n').split("\n\n")
    stack_str = stack_file.split("\n")
    
    instruction_file = instruction_file.replace("move","").replace("from ","").replace("to ","").strip().split("\n")
    instructions = [i for i in instruction_file if i !=" "]
          
stacks = {int(i):[] for i in stack_str[-1] if i != " "}
indexes =[index for index, char in enumerate(stack_str[-1]) if char != " "]
#print(indexes)
#print(stack_str[:-1])

def displayStacks():
    print(f"stacks:\n")
    for stack in stacks:
        print(stack, stacks[stack])
    
def resetStacks():
    for stack_num  in stacks:
        stacks[stack_num].clear()

def loadStacks():
    for string in stack_str[:-1]:
        stack_num = 1
        for index in indexes:
            #print(index, indexes)
            if string[index] != " ":
                stacks[stack_num].insert(0,string[index])
            stack_num +=1

     
    
# ----------Part One --------------

loadStacks()

for instruction in instructions:
    instruction = instruction.strip().split(' ')
    instruction = [int(i) for i in instruction]

    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]

    for crate in range(crates):
        crate_removed = stacks[from_stack].pop()
        stacks[to_stack].append(crate_removed)
    #print(stacks)

# Imprimindo ----Part One ----- 

stack_end_p1=""    
for stack in stacks:
    #print(stacks)  
    stack_end_p1 += stacks[stack][-1]

print("\n\n--- Part One ---")
#displayStacks()
print(f"\n answer-> {stack_end_p1} \n")
 #VWLCWGSDQ

#---------------------------------
# ----------Part Two -------------
#---------------------------------
#print(stack_str[:-1])
resetStacks()
loadStacks()

for instruction in instructions:
    instruction = instruction.strip().split(' ')
    instruction = [int(i) for i in instruction]

    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]

    #caixas q devem ser removidas
    crates_to_remove = stacks[from_stack][-crates:]
    
    # remover
    stacks[from_stack]= stacks[from_stack][:-crates]
    
    for crate in crates_to_remove:
        stacks[to_stack].append(crate)


#Imprimindo ----Part Two -----

stack_end_p2=""
for stack in stacks:
    #print(stacks)
    stack_end_p2 += stacks[stack][-1]

print("\n\n--- Part Two ---")
#displayStacks()
print(f"\n answer-> {stack_end_p2} \n") #PNDDQWWWB | TCGLQSLPW
