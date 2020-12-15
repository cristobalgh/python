#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 21:33:12 2018

@author: cristobal
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    ant = 0
    for word in aDict:
        if len(aDict[word]) > ant:
            #ant = len(aDict[word])
            c = word
    return c