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

class gear:
    def __init__(self, sym, row, col, grid) -> None:
        self.sym = sym
        self.row = int(row)
        self.col = int(col)
        self.adj = count_adj_nums(grid, self)
    
    def get_ratio(self, nums):

        ratio = 1
        for no in nums:
            if (self.row >= no.row-1 and
                self.row < no.row+2 and
                self.col >= no.col_s-1 and
                self.col < no.col_e+1):
                ratio *= no.val
        return ratio
    
############################
# Functions

def part_one(grid, nums):

    total = 0
    for num in nums:
        total += num.val if is_sym_adj(grid, num) else 0
    return total

def is_sym_adj(grid, num) -> bool:

    for row in grid[num.row-1 : num.row+2]:
        for col in row[num.col_s-1 : num.col_e+2]:
            #print(col, end="")
            if re.match(r"[^\d\s\.a-zA-Z]", col):
                #print()
                return True
    return False

def part_two(grid, gears, nums):

    ratios = 0
    for gear in gears:
        if gear.adj == 2:
            ratios += gear.get_ratio(nums)
    
    return ratios

def count_adj_nums(grid, gear) -> int:

    count = 0
    for row in grid[gear.row-1 : gear.row+2]:
        #print(row[gear.col-1:gear.col+2])
        for m in re.findall(r"\d+", row[gear.col-1:gear.col+2]):
            count += 1
    #print("Adj count:", count)         

    return count

def pad_input(grid, padding="."):
    
    padded_grid = [f"{padding}{row}{padding}" for row in grid]
    padded_grid.insert(0, padding * len(padded_grid[0]))
    padded_grid.append(padding * len(padded_grid))

    return padded_grid

def day03(text):
    print("Day 03 - Gear Ratios")
    
    part1, part2 = text, ''
    
    grid = pad_input(tl.toList(text))
    
    #print(grid)
    nums = []
    gears = []

    for row_num, row in enumerate(grid):
        for m in re.finditer(r"\d+", row):
            nums.append(num(int(m.group(0)), row_num, m.start(0)))
        for m in re.finditer(r"\*", row):
            gears.append(gear(m.group(0), row_num, m.start(0), grid))
        
    part1 = part_one(grid, nums)
    part2 = part_two(grid, gears, nums)

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day03/inc" 
    
    # Change file
    #######
    file = "ex.txt"
    file = "in.txt"
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