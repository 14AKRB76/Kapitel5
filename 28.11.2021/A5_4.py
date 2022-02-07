# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 10:45:24 2021

@author: Michael
"""

##################################################################################
def AddAssing(A, B):
    if type(A[0]) == list and type(B[0]) == list:
        #print("yala Liste")
        if len(A) == len(B):
            #print("yala Len")
            if type(A[0][0]) == float or type(A[0][0]) == int and type(A[0][0]) == type(B[0][0]):
                #print("yala Typ")
                i = -1
                Az = A[:]
                for vektor in A:
                    i += 1
                    # print(i)
                    # print(vektor)
                    j = -1
                    for numb in vektor:
                        j += 1
                        # print(j)
                        # print(numb)
                        Az[i][j] = numb + B[i][j]

                A = Az
            else:
                print("falscher Datentyp")
        else:
            print("unterschiedliche Listenlaenge")
    elif type(A[0]) == type(B[0]) and type(A[0]) == int or type(A[0]) == float:
        k=-1
        Az = A[:]
        for numbi in A:
            k+=1
            Az[k] = numbi + B[k]
        A = Az
        
    else:
        print("falscher Datentyp")
    
    return A
##################################################################################
def Add(A, B):
    if type(A[0]) == list and type(B[0]) == list:
        #print("yala Liste")
        if len(A) == len(B):
            #print("yala Len")
            if type(A[0][0]) == float or type(A[0][0]) == int and type(A[0][0]) == type(B[0][0]):
                i= -1
                C = []
                
                for vektor in A:
                    vek= []
                    i+=1
                    j=-1
                    for numb in vektor:
                        j+=1
                        vek.append(A[i][j]+B[i][j])
                    C.append(vek)
            
                return C
            else:
                print("falscher Datentyp")     
        else:
            print("unterschiedliche Listenlaenge")
    elif type(A[0]) == type(B[0]) and type(A[0]) == int or type(A[0]) == float:
        C=[]
        k=-1
        for numbi in A:
            k+=1
            C.append(A[k] + B[k])
        return C
    else:
        print("Falsche Eingabe")
    
        
    
##################################################################################
##################################################################################



C = [[1, 2, 3], [1, 2, 3]]

D = [[5, 6, 8], [5, 6, 8]]


P = [1, 2, 3]

O = [5, 6, 1]

#print(AddAssing(C, D))

K = Add(P, O)
print(Add(P, O))