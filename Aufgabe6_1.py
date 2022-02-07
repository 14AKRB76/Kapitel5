# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:34:55 2020

@author: Pia
"""
#Skript zu Übungsvideo 9
#Modularisierung

###Externe Bibliotheken importieren

##Alle Funktionen eines Moduls importieren

#1.Möglichkeit 
# import math
# print(dir(math))
# print(math.__doc__)
# print(math.sqrt(16))

#2.Möglichkeit 
# import math as m
# print(dir(m))
# print(m.sqrt(16))

#3.Möglichkeit 
#NICHT zu empfehlen!
# from math import *
# print(sqrt(16))

#Einzelne Funktionen eines Moduls importieren
# from math import sqrt
# print(sqrt(16))

###Eigene Module importieren

##Alle Funktionen eines Moduls importieren

#1.Möglichkeit
# print(dir(Aufgabe5_1)) 
# import Aufgabe5_1
# print(Aufgabe5_1.berechne_Distanz([1,2,3],[2,3,4]))

#2.Möglichkeit 
# import Aufgabe5_1 as A
# print(dir(A)) 
# print(A.berechne_Distanz([1,2,3],[2,3,4]))

#3.Möglichkeit 
# from Aufgabe5_1 import *
# print(berechne_Distanz([1,2,3],[2,3,4]))

#Einzelne Funktionen eines Moduls importieren
# from Aufgabe5_1 import berechne_Distanz
# print(berechne_Distanz([1,2,3],[2,3,4]))



