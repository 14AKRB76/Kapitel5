# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 13:26:13 2021

@author: Michael
"""

def Obstkorb(Fruechte):
    """ Obst"""
    flist = Fruechte.split("; ")
    fdict = {}
    for name in flist:
        #print(name)
        if name not in fdict.keys():
            fdict[name] = 1
        elif name in fdict.keys():
            numb = flist.count(name)
            fdict[name] = numb
    
    return fdict, __Obstkorb__



######################




Fruechte = "Banane; Apfel; Banane; Birne; Birne"

print(Obstkorb(Fruechte))
