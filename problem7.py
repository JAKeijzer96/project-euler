'''
25/04/2020

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''

import math
# checking each 6n +- 1 number
def is_prime(n):
  if n <= 1:
    return False
  if n == 2 or n == 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i <= math.sqrt(n)+1:
    if n % i == 0 or n % (i+2) == 0:
      return False
    i += 6
  return True

primes = 0
number = 0
while primes < 10001:
  number += 1
  if is_prime(number):
    primes += 1

print(primes)
print(number)