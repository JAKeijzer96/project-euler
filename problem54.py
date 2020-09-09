'''
26/06/2020

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:
Hand	Player 1	 	    Player 2	 	Winner
1	 	5H 5C 6S 7S KD      2C 3S 8S 8D TD  Player 2
        Pair of Fives       Pair of Eights 	
2	 	5D 8C 9S JS AC	 	2C 5C 7D 8S QH	Player 1
        Highest card Ace    Highest card Queen
3	 	2D 9C AS AH AC	 	3D 6D 7D TD QD	Player 2
        Three Aces          Flush with Diamonds
4	 	4D 6S 9H QH QC      3D 6D 7H QD QS  Player 1
        Pair of Queens      Pair of Queens
        Highest card Nine   Highest card Seven
5	 	2H 2D 4C 4D 4S      3C 3D 3S 9S 9D  Player 1
        Full House          Full House
        With Three Fours    with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''

########
# PROGRAM FUNCTIONALITY:
# 
# read line from file (note: 10 is written as T)
# seperate into 2 hands
# call examine_hand on both hands
# check from royal flush down to high card
# if a player has a scoring combination that the other doesn't, stop checking:
#     full house vs flush or full house vs high card, full house wins either way
# if a player has a scoring combination and the other player has the same (eg one pair AA vs KK):
#     check for possible lower scoring combinations (both three of a kind, check for high card)
########

import collections
import time

def readfile(filename):
    with open(filename) as file:
        for line in file:
            hands = line.strip('\n').split(' ')
            yield hands[0:5], hands[5:10]

def examine_hand(hand):
    sameSuit = False
    values, suits = map(list, zip(*hand)) # zip returns two tuples (values) and (suits), map maps the list function to both tuples
    dic = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14} # dictionary used to replace 'TJQKA' values

    for idx, value in enumerate(values):
        if value in dic:
            values[idx] = dic[value] # replace 'TJQKA' with 10-14
    values = [int(value) for value in values] # convert 2-9 from str to int

    countedValues = collections.Counter(values) # count occurences of each value
    sortedValues = sorted(countedValues) # sort values by ascending order
    mostCommon = countedValues.most_common() # make list of tuples of most common cards and their frequency
    isStraight = sortedValues == [sorted(countedValues)[0] + i for i in range(5)] # check if it's a straight
    
    if all(x==suits[0] for x in suits): # suits only matter if they're all the same
        sameSuit = True
    
    return values, countedValues, sortedValues, mostCommon, isStraight, sameSuit

def evaluate(hands):
    player1, player2 = True, False # return values
    hand_1, hand_2 = hands[0], hands[1]
    values_1, countedValues_1, sortedValues_1, mostCommon_1, isStraight_1, sameSuit_1 = examine_hand(hand_1)
    values_2, countedValues_2, sortedValues_2, mostCommon_2, isStraight_2, sameSuit_2 = examine_hand(hand_2)

    # Royal Flush
    if sameSuit_1 and sortedValues_1 == [10,11,12,13,14]: # hand_1 royal flush
        return player1
    elif sameSuit_2 and sortedValues_2 == [10,11,12,13,14]: # hand_2 royal flush
        return player2
    
    # Straight Flush
    elif sameSuit_1 and isStraight_1: # hand_1 straight flush
        if sameSuit_2 and isStraight_2: # hand_2 also straight flush
            if sortedValues_1[0] > sortedValues_2[0]: # hand_1 higher straight
                return player1
            else: # sorted_2[0] > sorted_1[0]: # hand_2 higher straight
                return player2
        return player1 # hand_1 straight flush and hand_2 not equal or higher
    elif sameSuit_2 and isStraight_2: # hand_2 straight flush and hand_1 not equal or higher
        return player2

    # Four of a kind
    elif mostCommon_1[0][1] == 4: # four of a kind
        if mostCommon_2[0][1] == 4: # hand_2 also four of a kind
            if mostCommon_1[0][0] > mostCommon_2[0][0]: # player1 has higher four of a kind
                return player1
            else: # player2 has higher four of a kind
                return player2
            # no need to check for same value four of a kind since it's not possible
        return player1 # hand_1 four of a kind and hand_2 not equal or higher
    elif mostCommon_2[0][1] == 4: # hand_2 four of a kind and hand_1 not equal or higher
        return player2

    # Full House
    elif mostCommon_1[0][1] == 3 and mostCommon_1[1][1] == 2: # hand_1 full house
        if mostCommon_2[0][1] == 3 and mostCommon_2[1][1] == 2: # hand_2 full house
            if mostCommon_1[0][0] > mostCommon_2[0][0]: # hand_1 higher three cards
                return player1
            elif mostCommon_2[0][0] > mostCommon_1[0][0]: # hand_2 higher three cards
                return player2
            elif mostCommon_1[1][0] > mostCommon_2[1][0]: # hand_1 higher two cards
                return player1
            else: # hand_2 higher two cards
                return player2
        return player1 # hand_1 full house and hand_2 not equal or higher
    elif mostCommon_2[0][1] == 3 and mostCommon_2[1][1] == 2: # hand_2 full house and hand_2 not equal or higher
        return player2
    
    # Flush
    elif sameSuit_1: # hand_1 flush
        return player1
        # TODO
    elif sameSuit_2: # hand_2 flush and hand_1 not equal or higher
        return player2

    # Straight
    elif isStraight_1: # hand_1 straight
        if isStraight_2:
            if sortedValues_1[0] > sortedValues_2[0]: # hand_1 higher straight
                return player1
            else: # hand_2 higher straight
                return player2
        return player1 # hand_1 straight and hand_2 not equal or higher
    elif isStraight_2: # hand_2 straight and hand_1 not equal or higher
        return player2
    
    # Three of a Kind
    elif mostCommon_1[0][1] == 3: # hand_1 three of a kind
        if mostCommon_2[0][1] == 3: # hand_2 also three of a kind
            if mostCommon_1[0][0] > mostCommon_2[0][0]: # hand_1 higher three of a kind
                return player1
            else: # hand_2 higher three of a kind
                return player2
            # no need to check for same value three of a kind since it's not possible
        return player1 # hand_1 three of a kind and hand_2 not equal or higher
    elif mostCommon_2[0][1] == 3: # hand_2 three of a kind and hand_1 not equal or higher
        return player2

    # Two Pair
    elif mostCommon_1[0][1] == 2 and mostCommon_1[1][1] == 2: # hand_1 two pair
        if mostCommon_2[0][1] == 2 and mostCommon_2[1][1] == 2: # hand_2 also two pair
            if (max(mostCommon_1[0][0], mostCommon_1[1][0]) > # hand_1 higher high pair
                max(mostCommon_2[0][0], mostCommon_2[1][0])):
                return player1
            elif (max(mostCommon_2[0][0], mostCommon_2[1][0]) > # hand_2 higher high pair
                max(mostCommon_1[0][0], mostCommon_1[1][0])):
                return player2
            elif (min(mostCommon_1[0][0], mostCommon_1[1][0]) > # hand_1 higher low pair
                min(mostCommon_2[0][0], mostCommon_2[1][0])):
                return player1
            elif (min(mostCommon_2[0][0], mostCommon_2[1][0]) > # hand_2 higher low pair
                min(mostCommon_1[0][0], mostCommon_1[1][0])):
                return player2
            else:
                if mostCommon_1[2][0] > mostCommon_2[2][0]: # hand_1 higher high card
                    return player1
                else: # hand_2 higher high card
                    return player2
        return player1 # hand_1 two pair and hand_2 not equal or higher
    elif mostCommon_2[0][1] == 2 and mostCommon_2[1][1] == 2: # hand_2 two pair and hand_1 not equal or higher
        return player2
    
    # One Pair
    elif mostCommon_1[0][1] == 2: # hand_1 one pair
        if mostCommon_2[0][1] == 2: # hand_2 also one pair
            if mostCommon_1[0][0] > mostCommon_2[0][0]: # hand_1 higher pair
                return player1
            elif mostCommon_2[0][0] > mostCommon_1[0][0]: # hand_2 higher pair
                return player2
            else:
                countedValues_1.popitem() # remove pair
                countedValues_2.popitem()
                sortedValues_1 = sorted(countedValues_1) # can't do sort and pop in one line because popitem returns the
                sortedValues_2 = sorted(countedValues_2) # popped item so you would sort that instead of the new list
                for i in range(-1,-4, -1): # loop through 1st, 2nd and 3rd-highest cards
                    if sortedValues_1[i] > sortedValues_2[i]: # hand_1 higher card
                        return player1
                    if sortedValues_2[i] > sortedValues_1[i]: # hand_2 higher card
                        return player2
                raise ValueError('One pair loop: All cards are exactly the same') # we should never see this
        return player1 # hand_1 one pair and hand_2 not equal or higher
    elif mostCommon_2[0][1] == 2: # hand_2 one pair and hand_1 not equal or higher
        return player2

    # High Card
    elif all(mostCommon_1[i][1] for i in range(5)) and all(mostCommon_2[i][1] for i in range(5)): # extra check to see there's one of each
        for i in range(-1,-6, -1): # loop through all cards
            if sortedValues_1[i] > sortedValues_2[i]: # hand_1 higher card
                return player1
            if sortedValues_2[i] > sortedValues_1[i]: # hand_2 higher card
                return player2
        raise ValueError('High card loop: All cards are exactly the same') # we should never see this    
    else:
        raise ValueError(f'Error: no score or hand found. Hand: {hand_1}')

hand1Wins = 0
hand2Wins = 0

start = time.time()

for (hand1, hand2) in readfile('problem54.txt'):
    evaluate((hand1,hand2))
    if evaluate((hand1, hand2)):
        hand1Wins += 1
    else:
        hand2Wins += 1

print(f'Hand 1 wins {hand1Wins} hands')
print(f'Hand 2 wins {hand2Wins} hands')
print(f'Evaluated all hands in {time.time()-start:.3f} seconds')
