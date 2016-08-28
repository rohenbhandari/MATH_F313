import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return (x**2 - 5) 

check = 10**-3 #Precision of decimal places
for a in range(-10, 10):
  for b in range(-a, a):
    if f(a) * f(b) < 0:
      break
    break

i = 1

while abs(a - b) > check:
  c = (a + b) / 2.0
  if(f(c) * f(a) < 0.0):
    b = c
  elif(f(c) * f(b) < 0.0):
    a = c
  i += 1

c = (a+b)*.5
print c, i
