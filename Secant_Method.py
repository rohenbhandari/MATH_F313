import timeit

start = timeit.timeit()

import math
import numpy as np
import matplotlib.pyplot

def f(x):
  return (x - 1) * (x + 5.0)

check = 10**-3 #used for precision checking

for a in range(-10, 10):
  for b in range(-a, a):
    if (f(a) * f(b) < 0):
      break
    break

while abs(b - a) > check:
  c = b - ((f(b) * (b - a))) / (f(b) - f(a))
  a = b
  b = c

print c, f(c)

end = timeit.timeit()

print start - end
