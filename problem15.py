'''
27/04/2020

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

'''


# For a 20x20 grid, to move from (0,0) to (20,20) we must move east (E) 20 times,
# and move south (S) 20 times. We can count the number of unique solutions by
# counting the number of unique permutations of the word EEEEEEEEEEEEEEEEEEEEEEEEESSSSSSSSSSSSSSSSSSSS
# 
# The number of permutations of n distinct objects is n!
# Unfortunately for us, our objects are not distinct
# 
# We can use the formula found at https://en.wikipedia.org/wiki/Permutation#Permutations_of_multisets
# and apply it to our set, with M = EEEEEEEEEEEEEEEEEEEEEEEEESSSSSSSSSSSSSSSSSSSS, m1 = 20 and m2 = 20
# We then arrive at M!/(m1! * m2!) = 40!/(20! * 20!) = 137846528820
# 
# Extra reading at https://en.wikipedia.org/wiki/Lattice_path
# and https://en.wikipedia.org/wiki/Permutation
# and https://en.wikipedia.org/wiki/Permutation#Permutations_with_repetition
# and https://en.wikipedia.org/wiki/Permutation#Permutations_of_multisets

from math import factorial

print(int(factorial(40)/(factorial(20)*factorial(20))))
