# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:34:57 2017

@author: Mayur
"""

# =============================================================================
# Problem 7
# 
# You are given the following superclass. Do not modify this.
# 
# class Container(object):
#     """ Holds hashable objects. Objects may occur 0 or more times """
#     def __init__(self):
#         """ Creates a new container with no objects in it. I.e., any object 
#             occurs 0 times in self. """
#         self.vals = {}
#     def insert(self, e):
#         """ assumes e is hashable
#             Increases the number times e occurs in self by 1. """
#         try:
#             self.vals[e] += 1
#         except:
#             self.vals[e] = 1
#     def __str__(self):
#         s = ""
#         for i in sorted(self.vals.keys()):
#             if self.vals[i] != 0:
#                 s += str(i)+":"+str(self.vals[i])+"\n"
#         return s
# Write a class that implements the specifications below. Do not override any 
# methods of Container.
# 
# class Bag(Container):
#     def remove(self, e):
#         """ assumes e is hashable
#             If e occurs in self, reduces the number of 
#             times it occurs in self by 1. Otherwise does nothing. """
#         # write code here
# 
#     def count(self, e):
#         """ assumes e is hashable
#             Returns the number of times e occurs in self. """
#         # write code here
# For example,
# d1 = Bag()
# d1.insert(4)
# d1.insert(4)
# print(d1)
# d1.remove(2)
# print(d1)
# prints
# 4:2
# 4:2
# For example,
# d1 = Bag()
# d1.insert(4)
# d1.insert(4)
# d1.insert(4)
# print(d1.count(2))
# print(d1.count(4))
# prints
# 0
# 3
# 
# =============================================================================

#code
class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

# modified class Bag
class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        try:
            self.vals[e] -= 1
        except:
            return 0
        
    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        try:
            return self.vals[e]
        except:
            return 0
