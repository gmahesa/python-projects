# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 21:07:13 2019

@author: G_MAHESA99
"""

class bubblesort :
       array = []
       def __init__(self, arr):
              self.array = arr
       
       def sorting(array) :
              LOA = len(array)-1
              for i in range(LOA):
                     for j in range(LOA - i):
                            if array[j] > array[j+1]:
                                 array[j], array[j + 1] = array[j + 1], array[j]
              return array

       
list = [10,2,4,3,9,1,8,7,6,5]
sort = bubblesort(list)
print(sort.array)
       
        
        
           
    
       
       
       
       
       
       
       
       