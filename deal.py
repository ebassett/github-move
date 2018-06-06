#!/usr/bin/env python2

# -----------
# User Instructions
#
# Write a function, deal(numhands, n=5, deck), that
# deals numhands hands with n cards each.
#

import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n=5, deck=mydeck):
    random.shuffle(deck)
    hands = [ [] for _ in range(numhands) ]
    for _ in range(n):
        for hand in hands:
            hand.append(deck.pop())
    return hands

# This is how Peter Norvig did it (after shuffling).
# I made mine more complicated in order to deal out the way that you actually do it.
#    return [deck[n*i:n*(i+1)] for i in range(numhands)]

if __name__ == '__main__':
    print deal(3)

