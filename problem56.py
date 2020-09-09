'''
26/04/2020

A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
'''
import time
start = time.time()

max_sum = 0
current_sum = 0
for i in range(50,100):
    for j in range(50,100):
        current_sum = 0
        for digit in str(i**j):
            current_sum += int(digit)
        if current_sum > max_sum:
            max_sum = current_sum

print(max_sum)
