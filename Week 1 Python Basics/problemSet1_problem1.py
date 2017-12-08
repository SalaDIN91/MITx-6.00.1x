# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 02:18:23 2017

@author: Mayur
"""
"""
Problem 1

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if 
s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""

#code
count=0
for letter in s:
  if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
    count+=1
print("Number of vowels:",count)