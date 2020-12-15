#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 22:17:10 2018

@author: cristobal
"""
balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12.0
balancef = balance #parto debiendo todo
low = balance/12.0
high = (balance*(1+monthlyInterestRate)**12)/12.0
epsilon = 0.01 #to the cent...
pagoMensual=(high+low)/2.0
 
while abs(balancef) >= epsilon:
    balancef=balance
    for i in range(0,12):
        balancef = (balancef - pagoMensual)*(1+monthlyInterestRate)
        #print(str(balancef))
    if balancef < 0:
        high=pagoMensual
    else:
        low=pagoMensual
    pagoMensual=(high+low)/2.0
    #print(str(balancef))
print('Lowest Payment: '+str(round(pagoMensual,2)))
#print('balancef: '+str(balancef))
#print('balance: '+str(balance))#3