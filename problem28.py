'''
27/04/2020 (Solved ~3 minutes after reading the question whoo)

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

'''

# Start at 1
# Then 3,5,7,9 are seperated by 2 (3x3 square)
# 13, 17, 21, 25 are seperated by 4 (5x5 square)
# 31, 37, 43, 49 are seperated by 6 (7x7 square)

end_sum = 1
number = 1
increment = 2
for _ in range(500):
    for _ in range(4):
        number += increment
        end_sum += number
    increment += 2

print(end_sum)