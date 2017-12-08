# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 14:10:30 2017

@author: Mayur
"""
"""
Exercise 4:
    
Write a Python function that returns the sublist of strings in aList
that contain fewer than 4 characters.
For example, if aList = ["apple", "cat", "dog", "banana"],
your function should return: ["cat", "dog"]

This function takes in a list of strings and returns a list of strings.
Your function should not modify aList.
"""

#code
def lessThan4(aList):
    '''
    aList: a list of strings
    returns: a list of strings having length of all the elements in  
    '''
    lenLessThan4 = []
    for elem in aList:
        if len(elem) < 4:
            lenLessThan4.append(elem)
    return lenLessThan4