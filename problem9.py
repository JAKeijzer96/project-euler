'''
25/04/2020

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''

import math

for a in range(1,1000):
  for b in range(1,1000):
   c_squared = a**2 + b**2
   if math.sqrt(c_squared) == int(math.sqrt(c_squared)):
     c = int(math.sqrt(c_squared))
     if a+b+c == 1000:
       print('a: ', a, ' b: ', b, ' c: ', c, ' product: ', a*b*c)