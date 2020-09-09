'''
27/04/2020

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

Note: Once the chain starts the terms are allowed to go above one million.
'''
largest_chain = 0
chain = 0
largest_number = 0

def collatz(n):
    global chain
    chain += 1
    if n % 2 == 0: # even
        #print('even:', n)
        while n % 2 == 0:
            n = n//2
            if n == 1:
                return 1
        return collatz(n)
    elif n % 2: # odd
        #print('odd:', n)
        # 3 * odd + 1 is always even, so do next step already
        n = 3 * n + 1
        while n % 2 == 0 and n > 2:
            n = n//2
        return collatz(n)


for number in range(1, 1000000):
    collatz(number)
    if chain > largest_chain:
        largest_chain = chain
        largest_number = number
    chain = 0

print('number:', largest_number, 'has chain: ', largest_chain)
    
