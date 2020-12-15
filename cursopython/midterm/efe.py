#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 17:58:47 2018

@author: cristobal
"""
def f(a,b):
    return a+b

def score(word,f):
    puntos=[]
    m=0
    for i in word.lower():
        puntos.append(m*(ord(i)-96))
        m+=1
    puntos.sort()
    puntos.reverse()
    return f(puntos[0],puntos[1])