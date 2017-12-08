# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 02:24:55 2017

@author: Mayur
"""
"""
Problem 2

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

#code
bob = 0
start = 0
end = 3
while end <= len(s) and start < len(s)-2 :
    if s.count('bob', start,end) == 1:
        bob += 1
    start += 1
    end += 1

print("Number of times bob occurs is:",bob)