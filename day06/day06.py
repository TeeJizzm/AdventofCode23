## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 06

############################
# Imports

import os

import tools.texttolists as tl

import re
import numpy as np
import math

############################
# Variables



############################
# Functions

def calc_beating_record(time, dist):

    results = []
    ## Quadratics
    # y = (-1)x^2 + (t)x + 0 
    # a = -1
    # b = t
    # c = -d
    for t, d in zip(list(map(int, re.findall(r"\d+", time))), list(map(int, re.findall(r"\d+", dist)))):
        
        lower = (-t + math.sqrt(t**2 - 4*d)) / (-2)
        upper = (-t - math.sqrt(t**2 - 4*d)) / (-2)

        results.append(math.floor(upper-1e-7) - math.ceil(lower+1e-7) + 1)
    return results

def day06(text):
    print("Day 06 - Wait for it")
    
    part1, part2 = 0, 0
    
    time, dist = tl.toList(text)
    time = time.split(":")[-1]
    dist = dist.split(":")[-1]
    part1 = math.prod(calc_beating_record(time, dist))
    part2 = math.prod(calc_beating_record(str.replace(time, " ", ""), str.replace(dist, " ", ""))) # Make the string a single number each
    
    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day06/inc" 
    
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

    part1, part2 = day06(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############