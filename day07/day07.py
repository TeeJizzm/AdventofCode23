## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 07

############################
# Imports

import os

import tools.texttolists as tl

from statistics import mode

############################
# Variables

CARDS = {"A": 14, "K": 13,
         "Q": 12, "J": 11,
         "T": 10, "9": 9,
         "8": 8, "7": 7,
         "6": 6, "5": 5,
         "4": 4, "3": 3,
         "2": 2, "1": 1}

CARDS2 = {"A": 14, "K": 13,
         "Q": 12, "T": 10, 
         "9": 9, "8": 8, 
         "7": 7, "6": 6, 
         "5": 5, "4": 4, 
         "3": 3, "2": 2, 
         "1": 1, "J": 0,}

class player:
    def __init__(self, cards, bet) -> None:
        self.cards = cards
        self.bet = int(bet)
        self.cardvals = [CARDS[card[0]] for card in cards]
        self.cardvals2 = [CARDS2[card[0]] for card in self.cards]
        self.hand_score = hand_score(cards)
        self.hand_score2 = hand_score2(cards)

############################
# Functions

def hand_score(cards) -> int:

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

def hand_score2(cards) -> int:

    cards_jokerless = str.replace(cards, "J", "")

    if cards_jokerless:
        cards_jk = str.replace(cards, "J", mode(cards_jokerless))
        return hand_score(cards_jk)
    else:
        return hand_score(cards)

def scoring(plays) -> (int, int):

    part1, part2 = 0, 0
    players = [player(cards, bet) for cards, bet in plays]

    # Sort players based on hand score first, then card value in order
    players.sort(key=lambda hand: (hand.hand_score, hand.cardvals[0], 
                                   hand.cardvals[1], hand.cardvals[2], 
                                   hand.cardvals[3], hand.cardvals[4]))
    
    for i, p in enumerate(players):
        part1 += (i+1) * p.bet

    # Sort players based on hand score first, then card value in order
    players.sort(key=lambda hand: (hand.hand_score2, hand.cardvals2[0], 
                                   hand.cardvals2[1], hand.cardvals2[2], 
                                   hand.cardvals2[3], hand.cardvals2[4]))

    
    for i, p in enumerate(players):
        part2 += (i+1) * p.bet

    return part1, part2


def day07(text):
    print("Day 07 - Camel Cards")
    
    plays = tl.to2dLists(text, "\n", " ")
        
    part1, part2 = scoring(plays)

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