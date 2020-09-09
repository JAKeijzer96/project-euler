'''
25/04/2020

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

import math

def largest_prime_factor(n):
    largest_factor = -1
    # while n is divisible by 2, divide it by 2
    while not (n % 2):
        n = n//2
        largest_factor = 2

    # loop until sqrt of the number
    for i in range(3, int(math.sqrt(n))+1, 2):
        while not (n % i):
            n = n/i
            largest_factor = i

    return largest_factor
    
print(largest_prime_factor(600851475143))
