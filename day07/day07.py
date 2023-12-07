## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 07

############################
# Imports

import os

import tools.texttolists as tl

############################
# Variables

CARDS = {"A": 14, "K": 13,
         "Q": 12, "J": 11,
         "T": 10, "9": 9,
         "8": 8, "7": 7,
         "6": 6, "5": 5,
         "4": 4, "3": 3,
         "2": 2, "1": 1}

class player:
    def __init__(self, cards, bet) -> None:
        self.cards = cards
        self.bet = int(bet)
        self.hand_score = hand_score(cards)
        self.cardvals = [CARDS[card[0]] for card in cards]

############################
# Functions

def hand_score(cards):

    match len({*cards}):
        case 1: # 5 of a kind
            return 6
        case 2: # 4 of a kind OR full house
            if [*cards].count([*cards][0]) in [1, 4]:
                # 4 of a kind
                return 5
            elif [*cards].count([*cards][0]) in [2, 3]:
            # Full House
                return 4
        case 3: # 3 of a kind or 2 pair
            for card in cards:
                if [*cards].count(card) == 3:
                    # 3 of a kind
                    return 3
                elif [*cards].count(card) == 2:
                    # 2 pair
                    return 2
        case 4: # 1 pair
            return 1
        case 5: # No matches, card high
            return 0

def part_one(plays) -> int:

    total = 0
    players = [player(cards, bet) for cards, bet in plays]

    for p in players:
        print(p.cards, p.hand_score)

    # Sort players based on hand score first, then card value in order
    players.sort(key=lambda hand: (hand.hand_score, hand.cardvals[0], 
                                   hand.cardvals[1], hand.cardvals[2], 
                                   hand.cardvals[3], hand.cardvals[4]))
    
    for i, p in enumerate(players):
        total += (i+1) * p.bet
    return total


def day07(text):
    print("Day 07 - Camel Cards")
    
    part1, part2 = text, ''
    
    plays = tl.to2dLists(text, "\n", " ")
        
    part1 = part_one(plays)

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day07/inc" 
    
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

    part1, part2 = day07(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############