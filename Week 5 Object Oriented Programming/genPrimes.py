# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 18:46:51 2017

@author: Mayur
"""

# =============================================================================
# Exercise: genPrimes
# 
# Write a generator, genPrimes, that returns the sequence of prime numbers on 
# successive calls to its next() method: 2, 3, 5, 7, 11, ...
# 
# Hints
# Ideas about the problem
# Have the generator keep a list of the primes it's generated. A candidate number 
# x is prime if (x % p) != 0 for all earlier primes p.
# 
# =============================================================================

#code
def genPrimes():
    primeList = [2]
    x = 3
    yield 2
    while True:
        flag = 0
        for p in primeList:
            if x % p == 0:
                flag = 1
                break
        if flag == 0:
            yield x
            primeList.append(x)
        x += 1