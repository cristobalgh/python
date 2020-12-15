#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 22:04:38 2018

@author: cristobal
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    i=0
    eTup = ()
    while i < len(aTup):
        eTup = eTup + aTup[i:i+1]
        i+=2
    return eTup