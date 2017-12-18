# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 13:21:19 2017

@author: Mayur
"""

# =============================================================================
# Problem 3
# 
# Write a function is_triangular that meets the specification below. A triangular 
# number is a number obtained by the continued summation of integers starting 
# from 1. For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 
# 1, 3, 6, 10, etc., are triangular numbers.
# 
# def is_triangular(k):
#     """
#     k, a positive integer
#     returns True if k is triangular and False if not
#     """
#     #YOUR CODE HERE
# =============================================================================

#code
def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    num = 1
    triangularNo = 0
    while triangularNo < k:
        triangularNo += num
        num += 1
    if triangularNo == k:
        return True
    return False





