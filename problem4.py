'''
25/05/2020

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''
# one possible optimisation: instead of looping from 0 to range, go backwards from range to 0
# however, is 98x100 bigger or 99x99? and 97x100 or 98x99? and so on
# at time of coding I couldn't be bothered figuring out

def largest_palindrome(range1, range2):
    result = 0
    for x in range(range1):
        for y in range(range2):
            number = x * y
            for digit in str(number):
                if str(number) == str(number)[::-1] and number > result:
                    result = number
    return result

print(largest_palindrome(1000, 1000))