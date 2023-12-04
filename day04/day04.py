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

    score = 0
    for num in playing:
        if num in winning:
            score += 1


    if score == 0: return 0
    return (pow(2, score-1))

def part_two(card, winning, playing, counts):

    # Reuse part 1 logic
    score = 0
    for num in playing:
        if num in winning:
            score += 1
    
    #print(card, counts[card], score)

    # increase future card counts by number of current card copies
    for i in range(1, score+1):
        counts[card + i] += counts[card]

    return counts


def day04(text):
    print("Day 04 - Scratchcards")
    
    part1, part2 = 0, 0
    
    cards = tl.to2dLists(text, "\n", ":")

    counts = [1] * len(cards)

    for col, (_, nums) in enumerate(cards):
        
        winning = re.findall(r"\d+", nums.split("|")[0])
        playing = re.findall(r"\d+", nums.split("|")[1])
        part1 += part_one(winning, playing)
        counts = part_two(col, winning, playing, counts)

    part2 = sum(counts)

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