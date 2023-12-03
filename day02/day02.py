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
        match col:
            case "red": 
                if int(cnt) > RED: return 0
            case "blue":
                if int(cnt) > BLU: return 0
            case "green":
                if int(cnt) > GRN: return 0
        
    return int(num) # game num val or 0


def day02(text):
    print("Day 02 - Cube Conundrum")
    
    part1, part2 = 0, 0
    
    lines = tl.toList(text)

    for game, reveal in tl.to2dLists(text, item=": "):

        hands = tl.to2dLists(reveal, "; ", ", ")

        reveal = str.replace(reveal, "; ", ", ")
        #print(reveal)
        pulls = tl.toList(reveal, ", ")

        #print(pulls)

        part1 += part_one(game.split()[-1], pulls)
    
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