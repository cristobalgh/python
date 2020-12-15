#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 15:13:02 2018

@author: cristobal
"""
def closest_power(base,num):
    #base > 1
    #num > 0
    if num == 1:
        return 0
    abajo = 0
    deltai = abs(num-base)
    if deltai == 0:
        return 1
    while (base**abajo <= num):
        abajo+=1
    delta1=abs(num - base**(abajo-1))
    delta2=abs(num - base**abajo)
    if delta1<=delta2:
        return abajo-1
    else:
        return abajo