#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 17:47:25 2018
@author: cristobal
"""
def gcdIter(a, b):
    '''
    a, b: positive integers    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    listo=False
    div = min(a,b)
    while listo==False:
        if b%div==0 and a%div==0:
            listo=True
        elif div==1:
            listo=True
        else:
            div-=1
    return div