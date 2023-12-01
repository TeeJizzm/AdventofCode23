## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 01

############################
# Imports

import os

import tools.texttolists as tl

############################
# Variables



############################
# Functions

def firstDigit(line):
    
    for i, c in enumerate(line):
        if c.isdigit():
            return int(line[i])


def day01(text):
    print("Day 01 - Trebuchet?!")
    
    part1, part2 = text, ''
    
    lines = tl.toList(text)

    part1 = 0

    for line in lines:
        part1 += (firstDigit(line)*10) + (firstDigit(line[::-1]))

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day01/inc" 
    
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

    part1, part2 = day01(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############