# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 20:23:12 2020

@author: Tutor
"""

def Negiere(A):
    """
    HALLO    
        
    """
    if type(A[0])==list:
        
        B=[]
        for Zeile in A:
            B.append(Zeile[:])
        #Matrix
        # m Zeilen und n Spalten
        for m in range(len(B)):
            for n in range(len(B[m])):
                B[m][n]= B[m][n]*-1.
    elif type(A[0])==int or type(A[0])==float:
        #Vektor
        B=A[:]
        for m in range(len(B)):
            B[m]=B[m]*-1.
    else:
        B="Falscher Datentyp!"
    return B

if __name__ == "__main__":

    A = [1,2]
    Aneg = Negiere(A)
    print(Aneg)    #-> Ausgabe: [-1,-2]
    print(A)       #-> Ausgabe: [1,2]
    B = [[1.2,2],[3,4.5]]
    Bneg = Negiere(B)
    print(Bneg)    #-> Ausgabe: [[-1.2,-2],[-3,-4.5]]
    print(B)       #-> Ausgabe: [[1.2,2],[3,4.5]]


print(Negiere.__doc__)

