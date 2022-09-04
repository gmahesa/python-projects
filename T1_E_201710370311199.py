# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 21:22:14 2019

@author: user1
"""

print("Membagi bilangan dan mencari kuadrat dari 2 hingga 10, yang tidak habis di modulo 2 \n")
def fun(x, y): 
  def adder(): 
    return map(lambda num: num ** 2, filter(lambda num: num % 2 == 0, range(x, y))) #filter, lambda, map
  return adder()

fc_function = list(fun(2,5)) #first class object

def smart_divide(func): #decorator, high order function
  def inner(a,b): 
    print("membagi",a,"dengan",b)
    if b == 0:
      print("\ntidak dapat dibagi dengan " +str(b))
      print("\nMengalihkan ke program kuadrat")
      return fc_function
    return func(a,b) #function as return value
  return inner #closure

@smart_divide #decorator
def divide(a,b):
  return a/b
divide(5,0)
