# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:02:10 2019

@author: G_MAHESA99
"""

def pangkatkan(x): 
    def angka(y):
        return y**x 
    return angka 

angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print ("angka =", angka, "\n")

for i in range (5):
       list = []  
       for j in angka:
              hasil = pangkatkan(i+1)
              list.append(hasil(j))
       print ("Hasil Pangkat", i+1 , "=", list, "\n")