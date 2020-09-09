'''
25/04/2020

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''

# Slow implementation! Use sieve instead

import math
def is_prime(n):
  if n <= 1:
    return False
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i <= math.sqrt(n)+1:
    if n % i == 0 or n % (i+2) == 0:
      return False
    i += 6
  return True

primes = [2,3]
number = 5
while number < 2000000:
  number += 2
  if is_prime(number):
    primes.append(number)

#print(primes)
print(sum(primes))