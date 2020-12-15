#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 23:03:51 2018

@author: cristobal
"""

import pandas as pd
cir = pd.read_csv('circuitosprueba.csv')

#print(cir)
#print(cir.loc[0:5,:])
#print(cir.loc[5][0])
#print(len(cir))

epcs = pd.read_csv('epcsprueba.csv')
#print(len(epcs))
#print(epcs.loc[:,"Lenght"])
#print(epcs)
print(epcs.head(1))

salida = pd.DataFrame(index=['0','1','2'], columns=['Circuito','EPC1','m'])
