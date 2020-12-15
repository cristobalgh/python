#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 00:28:22 2018

@author: cristobal
"""
vecesadivino = 0
epsilon = 0.01
adivino = 50
#valor = 3*adivino**3+2*adivino**2+adivino+50

while abs(3*adivino**3+2*adivino**2+adivino+50)>= epsilon:
    adivino = adivino - (3*adivino**3+2*adivino**2+adivino+50)/(9*adivino**2+4*adivino+1)
#    adivino = adivino - (adivino**2 -24)/(2*adivino) #nr
    vecesadivino+=1
print("La raiz del polinomio es "+str(adivino))
print("adivine "+str(vecesadivino)+" veces")