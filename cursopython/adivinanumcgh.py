#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 20:56:05 2018

@author: cristobal

"""
abajo = 0
arriba = 100
adivino = 0
ant = 0
guess = 50
res = 'h'
print("Please think of a number between 0 and 100!")
while not(adivino):
    print("Is your secret number " + str(guess) + "?")
    res = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly:")
    if res == 'l':
        ant = guess
        abajo = guess
        guess = (arriba-abajo)//2 + ant
    elif res == 'h':
        ant = guess
        arriba = guess
        guess = ant - (arriba-abajo)//2
    elif res == 'c':
        adivino = 1
    else:
        print("Sorry, I did not understand your input.")

print("Game over. Your secret number was: ", guess)