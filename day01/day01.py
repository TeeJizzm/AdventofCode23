## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 01

############################
# Imports

import os

import re

import tools.texttolists as tl

############################
# Variables

PATTERN = r"(?=(1|2|3|4|5|6|7|8|9|0|zero|one|two|three|four|five|six|seven|eight|nine))"

NUMS = {
    'zero':0,
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9
}

############################
# Functions

def firstDigit(line):
    
    for i, c in enumerate(line):
        if c.isdigit():
            return int(line[i])
        
    # If nothing, assume Part 2 and return 0
    return 0

def findFirstLastDigits(line):

    matches = re.findall(PATTERN, line)

    digits = NUMS.get(matches[0]), NUMS.get(matches[-1])

    return digits

def day01(text):
    print("Day 01 - Trebuchet?!")
    
    part1, part2 = text, ''
    
    lines = tl.toList(text)

    part1, part2 = 0, 0

    for line in lines:
        part1 += (firstDigit(line)*10) + (firstDigit(line[::-1]))
        a, b = findFirstLastDigits(line)
        part2 += (10*a + b)


    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day01/inc" 
    
    # Change file
    #######
    #file = "ex1.txt"
    #file = "ex2.txt"
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