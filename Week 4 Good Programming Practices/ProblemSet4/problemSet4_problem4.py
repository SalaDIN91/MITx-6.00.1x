# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 00:55:17 2017

@author: Mayur
"""

# =============================================================================
# Problem 4 - Hand Length
# 
# We are now ready to begin writing the code that interacts with the player. 
# We'll be implementing the playHand function. This function allows the user 
# to play out a single hand. First, though, you'll need to implement the helper 
# calculateHandlen function, which can be done in under five lines of code.
# 
# =============================================================================

from ps4a import *
#code
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    count = 0
    for letter in hand:
        for i in range(hand[letter]):
            count += 1
    return count