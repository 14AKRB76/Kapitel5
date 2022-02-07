# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 20:17:10 2021

@author: Michael
"""

def Negiere(A):
    Aneg = A[:]
    if type(A[0]) == list:
        for liste in Aneg:
            #print(liste)0
            i=-1
            for number in liste:
                i+=1
                liste[i] = -number
    if type(A[0]) == int or type(A[0]) == float:
        j = -1
        for knumber in Aneg:
            j+=1
            Aneg[j] = -knumber
    return Aneg
                
            
            
            






Kappa = [1,2,1]

print(Negiere(Kappa))