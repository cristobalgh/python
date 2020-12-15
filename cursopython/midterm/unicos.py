#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 16:25:21 2018

@author: cristobal
"""
def uniqueValues(aDict):
    valores=list(aDict.values())
    unicosval = []
    unicoskeys = []
    for i in valores:
        if valores.count(i)==1:
            unicosval.append(i)
    for target in unicosval:
        for key in aDict.keys():
            if aDict[key]==target:
                unicoskeys.append(key)
    return sorted(unicoskeys)