# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 13:07:59 2021

@author: Michael
"""

def Obstkorb(Fruechte):
    Fruchtliste =[]
    Fruchtliste = Fruechte.split("; ")
    FruchtDict= {}
    for Fruchtnamen in Fruchtliste:
        Fruchtanzahl = Fruchtliste.count(Fruchtnamen)
        FruchtDict[Fruchtnamen] = Fruchtanzahl
    return FruchtDict
    
    print("test")
    
    
    

Fruechte = "Banane; Apfel; Banane; Birne"
Fruchtkorb = Obstkorb(Fruechte)
print(Obstkorb(Fruechte))
