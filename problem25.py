'''
05/05/2020

The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

F1 = 1, F2 = 1, F3 = 2, F4 = 3, F5 = 5, F6 = 8, F7 = 13, F8 = 21, F9 = 34, F10 = 55, F11 = 89, F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

'''

# Function for nth fibonacci number - Space Optimisataion 
# Taking 1st two fibonacci numbers as 0 and 1 
  
def fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(1,n):
            a, b = b, a+b
        return b 
  
fib = 1
maxlength = 1000
while len(str(fibonacci(fib))) < maxlength:
    fib += 1
print('Fibonacci number', fib, 'has length', maxlength)