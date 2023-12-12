## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 11

############################
# Imports

import os

import tools.texttolists as tl

from itertools import combinations as combos

############################
# Variables

class galaxy:
    def __init__(self, row, col) -> None:
        self.row = int(row)
        self.col = int(col)
        self.dists = []
    def add_dist(self, dist) -> None:
        self.dists.append(dist)

############################
# Functions

def part_one(grid) -> int:

    #exp_grid = grid_expansion(grid, ".")
    e_rows, e_cols = find_expanded(grid, ".")
    galaxies = find_galaxies(grid, "#", e_rows, e_cols)

    for g1, g2 in list(combos(galaxies, 2)):
        dist = abs(g1.row - g2.row) + abs(g1.col - g2.col)
        g1.add_dist(dist)
    
    return sum([sum(gal.dists) for gal in galaxies])

def part_two(grid) -> int:

    e_rows, e_cols = find_expanded(grid, ".")
    galaxies = find_galaxies(grid, "#", e_rows, e_cols, 1000000)

    for g1, g2 in list(combos(galaxies, 2)):
        dist = abs(g1.row - g2.row) + abs(g1.col - g2.col)
        g1.add_dist(dist)
    
    return sum([sum(gal.dists) for gal in galaxies])

def find_galaxies(grid, g, e_rows=[], e_cols=[], exp=2):

    galaxies = []

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == g:
                r_offset = sum(map(lambda e_r: r > e_r, e_rows)) * (exp-1)
                c_offset = sum(map(lambda e_c: c > e_c, e_cols)) * (exp-1)
                galaxies.append(galaxy(r_offset+r, c_offset+c))

    return galaxies

def grid_expansion(grid, s):

    exp_grid = grid[:]

    # Columns first
    for col_index in reversed(range(len(grid[0]))):
        if set([row[col_index] for row in grid]) == {s}:
            for r in exp_grid:
                r.insert(col_index, s)

    # Next rows
    for row_index, row in reversed(list(enumerate(grid))):
        if set(row) == {s}:
            exp_grid.insert(row_index, exp_grid[row_index])

    return exp_grid

def find_expanded(grid, s):
    e_rows, e_cols = [], []

    for c in range(len(grid[0])):
        if set([row[c] for row in grid]) == {s}:
            e_cols.append(int(c))
    
    for r, row in enumerate(grid):
        if set(row) == {s}:
            e_rows.append(int(r))

    return e_rows, e_cols

def day11(text):
    print("Day 11 - Cosmic Expansion")
    
    part1, part2 = '', ''
    
    grid = [[*row] for row in text.split("\n")]

    part1 = part_one(grid)
    part2 = part_two(grid)

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day11/inc" 
    
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

    part1, part2 = day11(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############