## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 08

############################
# Imports

import os

import tools.texttolists as tl

from itertools import cycle
import pandas as pd
import numpy as np
import re

############################
# Variables



############################
# Functions

def steps_to_match(instructions, df, start, match):
    
    if start in df.index:
        curr_pos = start
    for i, instr in enumerate(cycle(instructions)):
        if re.match(match, curr_pos):
            return i
        curr_pos = df.at[curr_pos, instr]

def part_two(instructions, df):

    mask = df.index.str.contains(r"\w\wA")
    steps = []

    for start in df.index[mask].tolist():
        #print(start)
        steps.append(steps_to_match(instructions, df, start, r"\w\wZ"))

    return np.lcm.reduce(steps)

def day08(text):
    print("Day 08 - Haunted Wasteland")
    
    part1, part2 = 0, 0

    instructions, nodetext = tl.to2dLists(text, "\n\n", "\n")

    df = pd.DataFrame([re.findall(r"\w\w\w", each) for each in nodetext],
                      columns=["pos", "L", "R"])
    df.set_index("pos", inplace=True)

    part1 = steps_to_match(instructions[0], df, "AAA", "ZZZ")
    part2 = part_two(instructions[0], df)

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day08/inc" 
    
    # Change file
    #######
    #file = "ex.txt"
    #file = "ex1.txt"
    #file = "ex2.txt"
    file = "in.txt"
    #######
    
    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    # Open file, clean up memory after
    with open(filepath, "r") as file:
        
        text = file.read() # Read data

    part1, part2 = day08(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############