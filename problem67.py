'''
27/04/2020

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

Note: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 2^99 altogether! If you could check one trillion (10^12) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

'''
# Possible to clean up code using something like 'for row in reversed(triangle)' to loop backwards

triangle = []
with open('problem67.txt') as file:
    for line in file:
        list1 = [int(number) for number in line.split(' ')]
        triangle.append(list1)

def traverse_triangle():
    # work backwards through the rows and columns
    triangle_index = len(triangle)-1
    for row_index in range(triangle_index, 0, -1):
        for column_index in range(len(triangle[triangle_index])-1, 0, -1):
            # Start at the last line and work back up, using a + max(b, c)
            # Example: 63 + max(4, 62). Use this method to clear the entire last line
            triangle[row_index-1][column_index-1] += max(triangle[row_index][column_index-1], triangle[row_index][column_index])
        triangle.pop() # remove the last row as it's no longer relevant
        triangle_index -= 1

traverse_triangle()
print(triangle[0][0])