'''
22/06/2020

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

# First we have to find an upper bound. It turns out that with 7 digits, the
# highest sum of the factorial of the digits is 7*9! = 2540160. For 6 digits
# this is 6*9! = 2177280, which is greater than 999999. We shall therefore
# use 7*9! as our upper bound, even though it can almost certainly be shown that
# a lower upper bound is possible

# Update after solving the problem
# Original solution calculated the factorial for every digit in the loop
# However, explicitly precalculating the factorials only takes the runtime down
# from ~4.1 seconds to 3.9 seconds

from math import factorial
import time

start = time.time()

faclist = [factorial(i) for i in range(10)]
upperbound = 7*faclist[9]
endsum = 0

for i in range(3, upperbound):
    fac_digit_sum = 0    
    for digit in str(i):
        fac_digit_sum += faclist[int(digit)]
    if fac_digit_sum == i:
        endsum += i

print(endsum)
print(time.time() - start)