## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 03

############################
# Imports

import os

import tools.texttolists as tl

import re

############################
# Variables



############################
# Functions

def part_one():

    return 0

def part_two():

    return 0

def day03(text):
    print("Day 03 - Gear Ratios")
    
    part1, part2 = text, ''
    
    rows = tl.toList(text)

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day03/inc" 
    
    # Change file
    #######
    file = "ex.txt"
    #file = "in.txt"
    #######
    
    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    # Open file, clean up memory after
    with open(filepath, "r") as file:
        
        text = file.read() # Read data

    part1, part2 = day03(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############