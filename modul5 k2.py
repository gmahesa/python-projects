# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:43:01 2019

@author: G_MAHESA99
"""
import matplotlib.pyplot as plt

model_complexity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bias = [250, 200, 150, 100, 80, 60, 30, 15, 5, 0]
total_error = [250, 200, 150, 100, 120, 150, 170, 200, 210, 230]
variance = [0, 10, 20, 40, 50, 60, 80, 100, 120, 150]

plt.plot(model_complexity, variance, color='green',
         linestyle='solid', label='variance')
plt.plot(model_complexity, bias, color='red',
         linestyle='dashdot', label='bias^2')
plt.plot(model_complexity, total_error, color='blue',
         linestyle='dotted', label='total error')

plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.legend()
plt.show()