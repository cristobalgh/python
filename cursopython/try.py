#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 10:03:15 2018

@author: cristobal
"""

while True:
    try:
        n = input("Por favor ingresa un entero: ")
        n = int(n)
        break
    except ValueError:
        print("No ingresaste un entero!")
print("Gracias!")