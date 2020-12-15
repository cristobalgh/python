# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 13:25:39 2018
@author: cristobal.galleguill
"""

import csv
#from limpialista import limpialista
f = open('circuitos.csv')
circuitos = list(csv.reader(f))

e = open('epcs.csv')
epcs = list(csv.reader(e))

salida = []

#lista circuito - escalerilla - metros
#repite por cada escalerilla en la que aparece el circuito
#circuitos que no aparecen: 'no ruteados'
for circuito in circuitos[1:]: #sin header
    estaba = 0
    for fila in epcs[2:]:#sin header
        if circuito[0] in fila:
           salida.append(circuito + fila [0:1] + fila[9:10])
           estaba = 1
    if estaba == 0:
        salida.append(circuito + ['no ruteado'])

#trae a una fila todas las escalerillas en las que 
#esta el circuito
out = []
trabajo = []

for cir in salida:
    trabajo.append(cir[0])
    esta = 0
    for fila in salida:
        if cir[0] in fila:
            trabajo.extend(fila[1:3])
    for ya in out:
        if cir[0] in ya:
            esta = 1
    if esta != 1:
        out.append(trabajo)
    trabajo = []

del esta, estaba, trabajo, fila, cir, ya, salida, circuito

#recibe fila completa [cir, epc1, m1, epc2, m2,...,epc1,m1, etc]
def limpialista(a):
    salida = []
    salida.append(a[0])
    mtemp = 0
    for el in a[1:len(a):2]:
        if el not in salida:
            for i in range(1,len(a[1:]),2):
                if el == a[i]:
                    try:
                        mtemp+=int(a[i+1])
                    except ValueError:
                        mtemp
            salida.append(el)
            salida.append(mtemp)
            mtemp=0
    return salida

final = []

for fila in out:
    final.append(limpialista(fila))
    
del fila, out

myFile = open('ruteocircuitos.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(final)
     
print("Writing complete")