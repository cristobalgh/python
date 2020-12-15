#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 20:07:17 2018

@author: cristobal
"""
def polysum(n,s):
    import math
    area = 0.25*n*s**2/math.tan(math.pi/n)
    perimeter = n*s
    sum = area+perimeter**2
    return round(sum,4)