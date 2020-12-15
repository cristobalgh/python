#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 22:17:10 2018

@author: cristobal
"""
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

#print('Month 0 balance: '+str(round(balance,2)))

for i in range(1,13):
    balance = (balance-balance*monthlyPaymentRate)*(1+annualInterestRate/12)
    #print('Month '+str(i)+' balance: '+str(round(balance,2)))
print('Remaining balance: '+str(round(balance,2)))
    