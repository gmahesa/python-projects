# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 21:02:15 2019

@author: G_MAHESA99
"""
array = [10,2,4,3,9,1,8,7,6,5]
LOA = len(array) - 1   
for i in range(LOA):       
    for j in range(LOA - i):           
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            
print(array)