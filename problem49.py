'''
23/06/2020
17
The arithmetic sequence, 1487, 48, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''
import time

start = time.time()

# Make a generator which yields primes up to limit
def sieve_of_eratosthenes(limit):
    a = [True] * limit # Initialize the list
    a[0] = a[1] = False # 0 and 1 would break the algorithm

    for (i, isprime) in enumerate(a):
        if isprime:
            #yield i # yield for returning primes one at a time
            for n in range(i*i, limit, i): # mark multiples of i non-prime
                a[n] = False
    return a # we use return to return the full list instead of yielding

prime_list = []
for idx,prime in enumerate(sieve_of_eratosthenes(10000)):
    if prime and idx > 1000:
        prime_list.append(idx)

def we_can_only_use_a_return_statement_inside_a_function():
    for prime in prime_list:
        for i in range(2,5000-prime//2): #(10000-prime)//2 = 5000-prime//2
            if prime+i in prime_list and prime+2*i in prime_list: # check for arithmatic sequence
                if sorted(str(prime)) == sorted(str(prime+i)) == sorted(str(prime+2*i)): # check for permutations
                    print(prime, prime+i, prime+2*i)
                    if prime not in [1487, 4817, 8147]: # since we're told there is only one other
                        return                          # possibility we can end the loop once it's found

we_can_only_use_a_return_statement_inside_a_function()
print(f'The program ran for {time.time()-start} seconds')
