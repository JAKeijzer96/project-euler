'''
22/06/2020

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    163^4 = 1^4 + 6^4 + 3^4 + 4^4
    820^8 = 8^4 + 2^4 + 0^4 + 8^4
    947^4 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

# We arrive at this problem after solving problem 34. Here we also have to find
# an upper bound. Our upper bound will be 6*9^5 = 354294. Here, as well as in
# problem 34, a lower upper bound can certainly be mathematically proven to be
# correct. However, we will not take the time to figure that out (for now)

import time

start = time.time()

power_list = [i**5 for i in range(10)]
upperbound = 6*power_list[9]
endsum = 0

for i in range(2, upperbound):
    digit_sum = 0
    for digit in str(i):
        digit_sum += power_list[int(digit)]
    if digit_sum == i:
        endsum += i

print(endsum)
print(f'Program ran for {time.time()-start:.2f} seconds')