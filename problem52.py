'''
26/06/2020

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

import itertools

for i in itertools.count(1):
    if (sorted(str(i)) == sorted(str(2*i)) == sorted(str(3*i))
        == sorted(str(4*i)) == sorted(str(5*i)) == sorted(str(6*i))):
        print(i, 2*i, 3*i, 4*i, 5*i, 6*i)
        break