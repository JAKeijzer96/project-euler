'''
24/06/2020

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2    =     0.5
    1/3    =     0.(3)
    1/4    =     0.25
    1/5    =     0.2
    1/6    =     0.1(6)
    1/7    =     0.(142857)
    1/8    =     0.125
    1/9    =     0.(1)
    1/10    =     0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''


# The max amount of recurring cycles for 1/d is d-1. This has to do with the amount
# of different remainders possible when looping through x = x * 10 % d
# Small script for clarification:
# x = 0
# for i in range(10):
#     print(x, x/7, int(x/7), x*10/7, int(x*10/7), x*10%7, int(x*10%7))
#     x = x * 10 % 7

import itertools

def cycle_length(n):
    seen_digits = {}
    x = 1
    for i in itertools.count(): # keep counting upwards until a value is returned
        if x in seen_digits:
            return i - seen_digits[x]
        else:
            seen_digits[x] = i
            x = x * 10 % n

most_cycles = 0
for i in range(1,1000):
    l = cycle_length(i)
    if l > most_cycles:
        most_cycles = i

print(most_cycles)