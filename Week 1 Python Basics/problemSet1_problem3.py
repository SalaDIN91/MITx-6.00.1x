# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 02:26:43 2017

@author: Mayur
"""
"""
Problem 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur 
in alphabetical order. For example, if s = 'azcbobobegghakl', then your program 
should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should print

Longest substring in alphabetical order is: abc
"""

#code
r = ''
c = ''
for char in s:
  if (c == ''):
    c = char
    r = c
  elif (c[-1] <= char):
    c += char
    if (len(r)<len(c)):
        r = c
  else:
    c = char
print("Longest substring in alphabetical order is:",r)