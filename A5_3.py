# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 12:05:10 2021

@author: Michael
"""

def Negiere(A):
    Negativ = []
    for Eintrag in A:
        if type(Eintrag) == int or type(Eintrag) == float:
            Variable = Eintrag*-1
            Negativ.append(Variable)
        if type(Eintrag) == list:
             for Zahlen in Eintrag:
                 kleine_Variable = Zahlen *-1
                 Eintrag.append(kleine_Variable)
                 print(Eintrag)
             
                
                    
                
        
                
                
Kalle = [[1,3,[5,8,7]], [4,8,9,101]]

Negation = Negiere(Kalle)