# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:15:01 2019

@author: G_MAHESA99
"""

import matplotlib.pyplot as plt

x = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
plt.style.use('seaborn-dark')
plt.hist(x, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.xlabel("Range")
plt.ylabel("Banyak Nilai")
plt.title("Luaran Angka")
plt.show()