# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 15:07:08 2018

@author: cristobal.galleguill
"""

import random

def rolldie():
    return random.choice([1,2,3,4,5,6])

def rollcoin():
    return random.choice([0,1])

def rollN(n, fun):
    result = ''
    for i in range(n):
        result = result + str(fun())
    print(result)

def flip(numFlips):
    heads = 0.0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads +=1
    return heads/numFlips

def flipsim(NumFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(NumFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    return mean