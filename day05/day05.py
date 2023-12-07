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

def srs_to_drs(srs, drs, val):
    return (drs + (val - srs))

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
                if (current_num >= srs) and (current_num < (srs + lng)):
                    current_num = srs_to_drs(srs, drs, current_num)
                    break
        location.append(current_num)


    return min(location)

def part_two(seeds, almanac):

    minimum = []
    for start, length in pairwise(seeds):
        #print("Seed, length: ", start, length)
        curr_set = set(range(start, start + length))
        for mapping in almanac:
            next_set = set()
            sect_set = set()
            for drs, srs, lng in mapping:
                # If an intersection of (curr_start -> + curr_len) and (srs + lng)
                # max of lower bound, min of upper bound

                if intersect := set.intersection(curr_set, range(srs, srs+lng)):
                    sect_set.update(intersect)
                    #print(sect_set)
                    next_set.update(map(lambda val: srs_to_drs(srs, drs, val), intersect))
                
            next_set.update(curr_set - sect_set)
            #print(">",next_set)
            curr_set = set(sorted(next_set))

        minimum.append(min(curr_set))
    return min(minimum)

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
    #file = "ex.txt"
    file = "in.txt"
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