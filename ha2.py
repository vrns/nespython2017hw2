#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:05:07 2018

@author: v
"""

def sumThreeFive(n):
    sum = 0
    n = int(n)
    for x in range(0,n):
        if x%3 == 0 or x%5 == 0:
            sum = sum+x
        #print(sum, x)
    return sum
