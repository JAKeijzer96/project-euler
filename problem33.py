'''
24/06/2020

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

import time
start = time.time()

def func():
    for i in range(1,100):
        for j in range(1,100):
            if i == j or i > j: # we only want fractions less than 1 in value
                continue
            istr, jstr = str(i), str(j)
            for digit in istr:
                if digit != '0' and digit in jstr: # remove trivial cases
                    newi = istr.replace(digit, '')
                    newj = jstr.replace(digit, '')
                    if newi and newj: # can't cast '' to int
                        newi, newj = int(newi), int(newj)
                    if (newi and newj) and newi / newj == i / j: # don't allow division by 0
                        print(f'{i}/{j} == {newi}/{newj} == {newi/newj}')
                        yield newi, newj

# At first I tried multiplying the fractions as they came, however it turns out
# that 0.25 * 0.2 * 0.4 * 0.5 returns 0.010000000000000002, a lovely precision error
# Hence the longer, messier code below

#denominator = 1
#for fraction in func():
#    denominator *= fraction
#denominator = 1/denominator

top, bottom = [], []
denominator = 1
for fraction in func():
    top.append(fraction[0])
    bottom.append(fraction[1])
for number in bottom:
    denominator *= number
for number in top:
    denominator /= number
print(denominator)
print(f'The program ran for {time.time()-start:.5f} seconds')