## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 02

############################
# Imports

import os

import tools.texttolists as tl

############################
# Variables

RED = 12
GRN = 13
BLU = 14

############################
# Functions

def part_one (num, pulls):

    for pull in pulls:
        cnt, col = pull.split()
        cnt = int(cnt)
        match col:
            case "red": 
                if cnt > RED: return 0
            case "blue":
                if cnt > BLU: return 0
            case "green":
                if cnt > GRN: return 0
        
    return int(num) # game num val or 0

def part_two (pulls):
    power = 0
    red_max, blu_max, grn_max = 0, 0, 0

    for pull in pulls:
        cnt, col = pull.split()
        cnt = int(cnt)
        match col:
            case "red": 
                if cnt > red_max: red_max = cnt
            case "blue":
                if cnt > blu_max: blu_max = cnt
            case "green":
                if cnt > grn_max: grn_max = cnt

    print(red_max, blu_max, grn_max )
    power = red_max * blu_max * grn_max 


    return power


def day02(text):
    print("Day 02 - Cube Conundrum")
    
    part1, part2 = 0, 0
    
    lines = tl.toList(text)

    for gamenum, reveal in tl.to2dLists(text, item=": "):

        reveal = str.replace(reveal, "; ", ", ") # Don't care about each round
        #print(reveal)
        pulls = tl.toList(reveal, ", ")
        #print(pulls)

        part1 += part_one(gamenum.split()[-1], pulls)

        part2 += part_two(pulls)
    
    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day02/inc" 
    
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

    part1, part2 = day02(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############