#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 21:24:10 2018

@author: cristobal
"""

def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
          
foo(3)