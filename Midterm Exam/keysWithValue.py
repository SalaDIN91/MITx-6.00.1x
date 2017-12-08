# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 14:17:54 2017

@author: Mayur
"""
"""
Exercise 5:

Write a Python function that returns a list of keys in aDict with the value 
target. The list of keys you return should be sorted in increasing order. 
The keys and values in aDict are both integers. (If aDict does not contain 
the value target, you should return an empty list.)

This function takes in a dictionary and an integer and returns a list.
"""

#code
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    keys = []
    for key in aDict:
        if aDict[key] == target:
            keys.append(key)
    return sorted(keys)
