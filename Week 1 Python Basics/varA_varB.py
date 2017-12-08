# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 02:10:44 2017

@author: Mayur
"""
"""
Exercise: vara varb

Assume that two variables, varA and varB, are assigned values, either numbers 
or strings.

Write a piece of Python code that evaluates varA and varB, and then prints out 
one of the following messages:

"string involved" if either varA or varB are strings

"bigger" if varA is larger than varB

"equal" if varA is equal to varB

"smaller" if varA is smaller than varB
"""

#code
if type(varA)==str or type(varB)==str:
  print("string involved")
else:
  if varA>varB:
    print("bigger")
  elif varA==varB:
    print("equal")
  else:
    print("smaller")