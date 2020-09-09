'''
21/06/2020

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
import math
import time

def is_abundant(n):
    endsum = 1 # skip over adding 1 and n
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            # add both divisors, except if it is sqrt(n), then add it only once
            endsum += i if i == n//i else i + n//i
    return endsum > n

time1 = time.perf_counter()

# make a list of all abundant numbers
abundant_list = []
for i in range(12,28124):
    if is_abundant(i):
        abundant_list.append(i)

int_list = [0] * 28124 # initializing with the numbers instead
                       # of 0 takes ~100 times longer for this size

for idx in range(len(abundant_list)):
    for i in range(len(abundant_list)-idx):
        s = abundant_list[idx] + abundant_list[idx+i]
        if s < 28124 and int_list[s] == 0:
            int_list[s] = s

sum_of_ints = 0
for i in range(28124):
    if int_list[i] == 0:
        sum_of_ints += i

time2 = time.perf_counter()
print(f'Program ran for {time2-time1:.2f} seconds')
print(sum_of_ints)