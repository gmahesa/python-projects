# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:45:35 2019

@author: G_MAHESA99
"""

import matplotlib.pyplot as plt

model_complexity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bias = [250, 200, 150, 100, 80, 60, 30, 15, 5, 0]
total_error = [250, 200, 150, 100, 120, 150, 170, 200, 210, 230]
variance = [0, 10, 20, 40, 50, 60, 80, 100, 120, 150]

plt.scatter(model_complexity, variance, color='green',
            marker='s', label='variance')
plt.scatter(model_complexity, bias, color='red',
            marker='2', label='bias ^ 2')
plt.scatter(model_complexity, total_error, color='blue',
            marker='o', label='total error')

plt.legend(fontsize='x-small')
plt.show()