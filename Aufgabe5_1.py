# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 09:41:52 2020

@author: Pia
"""

#Aufgabe 5.1

#1. Funktion berechne_Distanz 
def berechne_Distanz(A,B):
    Distanz=((A[0]-B[0])**2+(A[1]-B[1])**2+(A[2]-B[2])**2)**0.5
    return Distanz

#2. Funktion minimale_Distanz
def minimale_Distanz(Liste):
    #Anfangswert für minimale Distanz definieren
    min_D=berechne_Distanz(Liste[0],Liste[1])
    #Anfangswerte der Indizes für die Punkte mit minimalem Abstand
    Index1=0
    Index2=1
    #print(min_D)
    #Durchlaufen aller relevanten Punktkombinationen
    for i1 in range(len(Liste)-1):
        for i2 in range(i1+1,len(Liste)):
            #print(i1,i2)
            Distanz=berechne_Distanz(Liste[i1],Liste[i2])
            #print(Distanz)
            #Überprüfen ob Distanz der Punktkombination kleiner ist als aktuelle minimale Distanz
            if Distanz<min_D:
                min_D=Distanz
                Index1=i1
                Index2=i2
    return [min_D,Index1,Index2]

#HAUPTPROGRAMM
# A=[1,2,3]
# B=[1,2,4]
# #Distanz=berechne_Distanz(A,B)
# #print(Distanz)
# C=[5,2,3]
# D=[1,2,4]
# m=minimale_Distanz([A,B,C,D])
# print(m)



