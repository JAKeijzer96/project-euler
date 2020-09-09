'''
21/06/2020

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
import time

endlist = []
# Generate permutations using Heap's Algorithm
# https://en.wikipedia.org/wiki/Heap%27s_algorithm
def heapPermutation(a, size, n):
    # if size becomes 1 then append the obtained permutation
    if (size == 1):
        # make a copy of the new permutation. This avoids ending up with a list of
        # identical references that were appended, but the object it references
        # changed with each cycle. That way we would end up with a list of identical values
        endlist.append(a[:])
        return

    for i in range(size): 
        heapPermutation(a,size-1,n)

        # if size is odd, swap first and last element,
        # else if size is even, swap ith and last element
        if size&1:
            a[0], a[size-1] = a[size-1],a[0]
        else:
            a[i], a[size-1] = a[size-1],a[i]
        

a = [0,1,2,3,4,5,6,7,8,9]
n = len(a)
time1 = time.perf_counter()
heapPermutation(a, n, n)
time2 = time.perf_counter()
print(f'Calculating all permutations took {time2-time1:.2f} seconds')
endlist.sort()
time3 = time.perf_counter()
print(f'Sorting all permutations took {time3-time2:.2f} seconds')
print(f'The 1000000th permutation of "0123456789" is {"".join(map(str,endlist[999999]))}')
