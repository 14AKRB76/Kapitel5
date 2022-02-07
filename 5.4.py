# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 09:21:39 2021

@author: Michael
"""

def AddAssign(A, B):
    if type(A[0]) is list:
        if len(A) is len(B) and len(A[0]) is len(B[0]):
            for i in range(len(A)):
                for j in range(len(A[0])):
                    A[i][j]+=B[i][j]
            return "True"
        else:
            return "False"
    else:
        if len(A) is len(B):
            for i in range(len(A)):
                A[i]+=B[i]
            return "True"
        else:
            return "False"
    
    
    
    
def Add(A, B):
    C=[]
    if type(A[0]) is list:
        if len(A) is len(B) and len(A[0]) is len(B[0]):
            
            for i in range(len(A)):
                L=[]
                for j in range(len(A[0])):
                    zahl = A[i][j]+ B[i][j]
                    L.append(zahl)
                C.append(L)
            return "True", C
        else:
            return "False"
    else:
        if len(A) is len(B):
            for i in range(len(A)):
                zahl = A[i] + B[i]
                C.append(zahl)
            return "True", C
        else:
            return "False"
    
    
    
C = [[4,5,6], [1,5,3]]


D= [[4,5,6], [1,2,3]]
 

Vektor=AddAssign(C, D)   
print(Vektor) 



V = [[4,8,6], [1,2,3]]

K = [[4,5,6], [9,2,3]]

Vaktor = Add(V, K)
print(Vaktor)