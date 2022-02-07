#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 11:27:56 2020

@author: tutor
"""

"""
Aufgabe 5.5
"""

def Obstkorb(Fruechte):
    string=Fruechte.split('; ')
    D={}
    for obst in string:
        D[obst]=string.count(obst)
    return D

if __name__=='__main__':
    Fruechte = "Banane; Apfel; Banane; Birne"
    print(Obstkorb(Fruechte))
    
    