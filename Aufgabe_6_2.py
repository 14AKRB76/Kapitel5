# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 20:28:56 2020

@author: Tutor
"""

import Aufgabe_5_3

Vektor=[1,2,3]
Matrix=[[1,2,3],[4,5,6],[7,8,9]]
print("Negierter Vektor:", Aufgabe_5_3.Negiere(Vektor))
print("Negierte Matrix:", Aufgabe_5_3.Negiere(Matrix))

#Importiere das Paket numpy mittels import numpy.

import numpy as np

#Definiere ensprechende Vektoren und Matrizen mit numpy.array(..). Verwende die gleichen Werte wie unter Punkt 2.

NumpyVektor = np.array(Vektor)
NumpyMatrix = np.array(Matrix)
print("Numpy Vektor: "), NumpyVektor
print("Numpy Matrix:\n"), NumpyMatrix
print("Typ:" , type(NumpyVektor))
                                                             
#Teste das Negieren (einfach mittels -) sowie das innere Produkt mit der Funktion numpy.dot(..).                  

print("Vektor negiert: " , -NumpyVektor)
print("Matrix negiert:\n" , -NumpyMatrix)