#!/usr/bin/env python2

# -----------
# User Instructions
#
# Modify the card_ranks() function so that cards with
# rank of ten, jack, queen, king, or ace (T, J, Q, K, A)
# are handled correctly. Do this by mapping 'T' to 10,
# 'J' to 11, etc...

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = [r for r,s in cards]
    mapping = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    for i in range(len(ranks)):
        rank = ranks[i]
        if rank in mapping.keys():
            ranks[i] = mapping[rank]
        else:
            ranks[i] = int(rank)
    ranks.sort(reverse=True)
    return ranks

print card_ranks(['AC', '3D', '4S', 'KH']) #should output [14, 13, 4, 3]

