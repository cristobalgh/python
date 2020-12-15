#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 22:17:10 2018

@author: cristobal
"""
balance = 320000
annualInterestRate = 0.2
pagoMensual = 0
balancef = 1

#print('Month 0 balance: '+str(round(balance,2)))

#for i in range(1,13):
#    balance = (balance-balance*monthlyPaymentRate)*(1+annualInterestRate/12)
    #print('Month '+str(i)+' balance: '+str(round(balance,2)))
#print('Remaining balance: '+str(round(balance,2)))
while balancef >= 0:
    balancef=balance
    pagoMensual+=1
    for i in range(0,12):
        balancef = (balancef - pagoMensual)*(1+annualInterestRate/12)
    #print(str(balancef))
print('Lowest Payment: '+str(pagoMensual))