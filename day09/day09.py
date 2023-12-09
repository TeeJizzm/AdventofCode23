## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 09

############################
# Imports

import os

import numpy as np

############################
# Variables



############################
# Functions

def get_next_in_set(seq):
    #print(seq)
    if any(seq) == 0:
        return 0

    return (seq[-1] + get_next_in_set(np.diff(seq)))

def day09(text):
    print("Day 09 - Mirage Maintenance")
    
    part1, part2 = 0, 0

    sequences = [list(map(int, line.split(" "))) for line in text.split("\n")]

    for seq in sequences:

        part1 += get_next_in_set(seq)
        seq.reverse()
        part2 += get_next_in_set(seq)

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day09/inc" 
    
    # Change file
    #######
    #file = "ex.txt"
    file = "in.txt"
    #######
    
    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    # Open file, clean up memory after
    with open(filepath, "r") as file:
        
        text = file.read() # Read data

    part1, part2 = day09(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############