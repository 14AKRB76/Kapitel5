#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:38:16 2020

@author: tutor
"""

"""
Aufgabe 5.4
"""

def AddAssign(A,B):
    if type(A[0]) is list:
        if len(A) is len(B) and len(A[0]) is len(B[0]):
            for i in range(len(A)):
                for j in range(len(A[0])):
                    A[i][j]+=B[i][j]
            return 'True'
        else:
            return 'False'
    else:
        if len(A) is len(B):
            for i in range(len(A)):
                A[i]+=B[i]
            return 'True'
        else:
            return 'False'
        
def Add(A,B):
    if type(A[0]) is list:
        if len(A) is len(B) and len(A[0]) is len(B[0]):
            C=[]
            for i in range(len(A)):
                L=[]
                for j in range(len(A[0])):
                    
                    zahl=A[i][j]+B[i][j]
                    L.append(zahl)
                C.append(L)
            return C
        else:
            return 'False'
            
    else:
        if len(A) is len(B):
            C=[]
            for i in range(len(A)):
                zahl=A[i]+B[i]
                C.append(zahl)
            return C
        else:
            return 'False'

if __name__=='__main__':
    A=[1,2,3]
    B=[1,2,3]
    print(AddAssign(A,B))
    print(A)
    print(B)
    A=[1,2,3]
    B=[1,2,3]
    print(Add(A,B))
    print(A)
    print(B)
    A=[[1,2,3],[1,1,1]]
    B=[[1,2,3],[1,1,1]]
    print(AddAssign(A,B))
    print(A)
    print(B)
    A=[[1,2,3],[1,1,1]]
    B=[[1,2,3],[1,1,1]]
    print(Add(A,B))
    print(A)
    print(B)