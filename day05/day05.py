## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 05

############################
# Imports

import os

import tools.texttolists as tl

import re
import numpy as np

############################
# Variables



############################
# Functions

def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)

def part_one(seeds, mappings):

    location = []

    for seed in seeds:
        current_num = seed
        for mapping in mappings:
            for drs, srs, lng in mapping:
                if (current_num >= srs) & (current_num < (srs + lng)):
                    current_num = drs + (current_num - srs)
                    break
        location.append(current_num)


    return min(location)

def part_two(seeds, mappings):

    location = []

    for seed, length in pairwise(seeds):
        print(seed, length)
        curr_start, curr_len = seed, length
        for mapping in mappings:
            for drs, srs, lng in mapping:
                # If an intersection of (curr_start -> + curr_len) and (srs + lng)
                # max of lower bound, min of upper bound
                pass
        location.append(curr_start)

    return min(location)

def day05(text):
    print("Day 05 - If You Give A Seed A Fertilizer")
    
    part1, part2 = 0, 0

    groups = tl.to2dLists(text, "\n\n", "\n")

    seeds = list(map(int, re.findall(r"\d+", str.split(groups[0][0], ":")[1]))) # Extract seed numbers
    maps = [[list(map(int, re.findall(r"\d+", dsr))) for dsr in x_to_y[1:]] for x_to_y in groups[1:]] # make a 3d list of lines of [destination, source, range] for each map

    #print(maps)

    part1 = part_one(seeds, maps)
    part2 = part_two(seeds, maps)

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day05/inc" 
    
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

    part1, part2 = day05(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############