# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 09:05:58 2018

@author: cristobal.galleguill
"""

f = open("prueba.txt", "r")
for line in f:
    print(line)
f.close()

f = open("prueba.txt", "w")
f.write("esto es una prueba")
f.write("para agregar lineas al archivo")
f.close()