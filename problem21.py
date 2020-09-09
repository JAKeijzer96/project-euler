'''
21/06/2020

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
import math

def add_divisors(n):
    total_sum = 1 # skip over 1 so we don't add 1 and n as divisors
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            #print(n, i, n//i)
            total_sum += i + n // i # add both divisors. If x/y = z then x/z = y
    return total_sum

result = 0
for i in range(10000):
    j = add_divisors(i)
    if i != j and i == add_divisors(j): # i != j filters out numbers like 1, 6, 28, 496, 8128
        result += i
        print(i, j)

print(result)