'''
18/06/2020

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

'''

# bin(n) returns the binary notation of n in a string, starting with '0b'. bin(5) returns '0b101'

# Loop over all numbers from 1 to 999999 and check if n is a palindrome
# in base 10 by reversing its string notation. If true, do the same in binary.
# Double slicing is to reverse, then cut the reversed 'b0' at the end

sum = 0
for n in range(1, 1000000):
    if str(n) == str(n)[::-1]:
        if bin(n)[2:] == bin(n)[::-1][:len(bin(n))-2]:
            sum += n

print(sum)