#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 21:16:45 2018

@author: cristobal
"""
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(animals):
    i = 0
    for word in animals:
        i += len(animals[word])
    return i