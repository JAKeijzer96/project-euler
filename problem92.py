'''
24/06/2020

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''

# Solved with slow method, knowing that a method where you save the visited numbers
# would be faster. However, I kept slightly messing that implementation up, so decided
# to use the slow method and fix the fast method after looking at other solutions

import time
start = time.time()

endsum = 0 # end sum used for slow method
arr = [0]*10000000 # initialize array for faster method
arr[1], arr[89] = 1, 89 # set 1 and 89 to their own value to avoid endless loops
squares = [0,1,4,9,16,25,36,49,64,81] # precalculate squares

def digit_squares(n):
    global endsum
    s = 0
    for digit in str(n):
        s += squares[int(digit)]
    if s == 1:
        return
    if s == 89:
        endsum += 1
        return
    else:
        digit_squares(s)

def array_digit_squares(n, visited_numbers):
    global arr
    s = 0
    for digit in str(n):
        s += squares[int(digit)] # sum up the square of each digit
    while not arr[s]: # while we haven't found a precalculated sum
        array_digit_squares(s, visited_numbers + [s]) # call the function again, add s to list of visited numbers
    for number in visited_numbers: # once we have arrived at a precalculated sum,
        arr[number] = arr[s] # assign the value of the end sum (either 1 or 89) to all visited numbers

def slow():
    for i in range(2,10000000): # with i up to 10 million this took ~71 seconds
        digit_squares(i)
    print(f'endsum is {endsum}')

def faster():
    for i in range(2,10000000): # with i up to 10 million this took ~12 seconds
        array_digit_squares(i, [i])
    print(f'{arr.count(89)} occurences of 89 in array')


#slow()
faster()

print(f'The program ran for {time.time()-start:.2f} seconds')