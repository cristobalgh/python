# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 13:25:39 2018
@author: cristobal.galleguill
"""

import csv
f = open('circuitosprueba.csv')
circuitos = list(csv.reader(f))

e = open('epcsprueba.csv')
epcs = list(csv.reader(e))
#print(epcs)

salida = []

#el circuito esta en esta escalerilla
for circuito in circuitos:
    #print(circuito)
    for fila in epcs:
        #print(fila)
        if set(circuito)<=set(fila):
           salida.append(circuito + fila [0:1] + fila[9:10])
        #else:
         #   salida.append('no esta')

#trae a una fila todas las escalerillas en las que 
#esta el circuito
i=0

while 1:
    if i == len(salida)-1:
        break
    if salida[i][0]==salida[i+1][0]:#si es el mismo circ
        salida[i]=salida[i]+salida[i+1][1:3]
        salida.pop(i+1)
    else:
        i+=1;    
         
#for i in range(len(salida)-1):
#    if i == len(salida):
#        break
#    if salida[i][0]==salida[i+1][0]:#si es el mismo circ
#        salida[i]=salida[i]+salida[i+1][1:3]
#        salida.pop(i+1)

#for i in range(len(salida)-1):
#    if i == len(salida):
#        break
#    if salida[i][0]==salida[i+1][0]:
#        salida[i]=salida[i]+salida[i+1][1:]
#        salida.pop(i+1)

#sal2=salida[:]

#i = 0
#for row in sal2:
#    if sal2[i][1]==sal2[i+1][1]:
#        sal2[i][2]=sal2[i][2]+sal2[i+1][2]
#        sal2.pop(i+1)
#    i+=1

#for i in range(len(sal2)-1):
#    if sal2[i][1]==sal2[i+1][1]:
#        sal2[i][2]=sal2[i][2]+sal2[i+1][2]
#        #sal2.pop(i+1)



##
#new_list = []
#new_list.append("una frase")
#print(new_list)

#attendee_email = []
#for row in csv_f:
#    attendee_email.append(row[2])
#print(attendee_email)
#
#f.close()
#s = open('salida.csv2','w')
#datos_sal=csv.writer(s)
#datos_sal.writer(s)