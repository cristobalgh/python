#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 18:50:35 2018

@author: cristobal
"""
def isIn(char, aStr):
    if len(aStr)==0:
        return False
    if len(aStr)==1 and char==aStr:
        return True
    i=len(aStr)//2
    if char==aStr[i]:
        return True
    elif char<aStr[i]:
        return isIn(char, aStr[:i])
    elif char>aStr[i]:
        return isIn(char, aStr[i+1:])
    else:
        return False