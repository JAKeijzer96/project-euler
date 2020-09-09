'''
27/04/2020

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

Note: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

'''

# Possible to clean up code using something like 'for row in reversed(triangle)' to loop backwards


triangle = [[75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

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