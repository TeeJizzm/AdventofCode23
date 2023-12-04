## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 04

############################
# Imports

import os

import tools.texttolists as tl

import re

############################
# Variables



############################
# Functions

def part_one(winning, playing):

    count = 0

    for num in playing:
        if num in winning:
            count += 1

    if count == 0: return 0
    return pow(2, count -1)

def day04(text):
    print("Day 04 - Scratchcards")
    
    part1, part2 = 0, 0
    
    cards = tl.to2dLists(text, "\n", ":")
    for _, card in cards:

        winning = re.findall(r"\d+", card.split("|")[0])
        playing = re.findall(r"\d+", card.split("|")[1])
        #print(winning)
        #print(playing)5

        part1 += part_one(winning, playing)

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day04/inc" 
    
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

    part1, part2 = day04(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############