#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 16:52:55 2018

@author: cristobal
"""
def vals(t,li):
    for i in t:
        if type(i)==int:
            li.append(i)
        else:
            vals(i,li)
    return li

def max_val(t):
    lista=[]
    return max(vals(t,lista))