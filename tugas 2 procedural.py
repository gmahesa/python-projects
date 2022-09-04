# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 20:46:30 2019

@author: G_MAHESA99
"""

def bubblesort(array):   
    LOA = len(array) - 1   
    for i in range(LOA):       
        for j in range(LOA - i):           
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

array = [10,2,4,3,9,1,8,7,6,5]
print (bubblesort(array))