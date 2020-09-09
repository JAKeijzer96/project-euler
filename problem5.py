'''
25/04/2020

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Solution: https://projecteuler.net/overview=005

'''

# Own attempt, got stuck, copied code, didn't fully understand,
# looked at solution for explanation
def divisible_no_remainder(r):
    result = r+1
    for i in range(r+1, 0, -1):
        while result % i:
            result += 1
    return result

print(divisible_no_remainder(20))


# Code copied from:
# https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-37.php
def greatest_common_denominator(x,y):
    return (y and greatest_common_denominator(y, x % y)) or x
def least_common_multiple(x,y):
    return x * y // greatest_common_denominator(x,y)

n = 1
for i in range(1, 21):
     n = least_common_multiple(n, i)
print(n)