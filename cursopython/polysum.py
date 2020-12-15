#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 20:07:17 2018

@author: cristobal
"""
#definition of function polysum
def polysum(n,s):
    #import math lib so we have available
    #pi number and tangent (tan) mathematical function
    import math
    #calculate area of the polygon using math lib
    area = 0.25*n*s**2/math.tan(math.pi/n)
    #calclate perimeter of the polygon    
    perimeter = n*s
    #calculate sum, value to return
    sum = area+perimeter**2
    #return sum, rounded to the 4th decimal
    return round(sum,4)