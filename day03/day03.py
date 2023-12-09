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

class num:
    def __init__(self, val, row, col) -> None:
        self.val = int(val)
        self.row = int(row)
        self.col_s = int(col)
        self.col_e = self.col_s + len(str(self.val))

class symbol:
    def __init__(self, sym, row, col) -> None:
        self.sym = sym
        self.row = int(row)
        self.col = int(col)

############################
# Functions

def part_one():

    return 0

def part_two():

    return 0

def pad_input(grid, padding="."):
    
    padded_grid = [f"{padding}{row}{padding}" for row in grid]
    padded_grid.insert(0, padding * len(padded_grid[0]))
    padded_grid.append(padding * len(padded_grid))

    return padded_grid



def day03(text):
    print("Day 03 - Gear Ratios")
    
    part1, part2 = text, ''
    
    rows = pad_input(tl.toList(text))
    
    print(rows)
    nums =[]

    for row_num, row in enumerate(rows):
        for m in re.finditer(r"\d+", row):
            nums.append(num(int(m.group[0]), row_num, m.start(0)))
        

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