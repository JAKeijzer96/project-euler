'''
28/06/2020

Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.
003020600   483921657
900305001   967345821
001806400   251876493
008102900   548132976
700000008   729564138
006708200   136798245
002609500   372689245
800203009   372689514
005010300	695417382

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above
'''

# The solution used a modified version of the script in the Computerphile video about sudoku's,
# a video which I saw way before starting Project Euler, and I had already copied and messed with the script
#
# Source video: https://www.youtube.com/watch?v=G_UYXzGuqvM

import numpy as np
import time

def possible(grid, y,x,n):
    '''
    Returns True if it is possible to put n in the sudoku grid
    with coordinates grid[y][x]
    Parameters:
        y (int): index of row
        x (int): index of column
        n (int): number we want to try
    '''
    for i in range(9):
        if grid[y][i] == n: # check row
            return False
    for i in range(9):
        if grid[i][x] == n: # check column
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    # check square
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

def solve(grid):
    global endsum
    '''
    Function to solve a sudoku by trying all possible numbers
    '''
    # find an empty square
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0: # if the square is empty
                for n in range(1,10): # numbers 1-9
                    if possible(grid,y,x,n):
                        grid[y][x] = n
                        solve(grid) # recursion with one less empty square
                        # if we hit a dead end with the previous choice, make the square
                        # blank again and try the next possible number
                        grid[y][x] = 0
                # if we tried all possible numbers in the empty square and none worked,
                # we're in a dead end and return to the previous call of solve()
                return grid
    # if we reach this part of the function all squares are full
    print(np.matrix(grid))
    endsum += int(str(grid[0][0]) + str(grid[0][1]) + str(grid[0][2]))

def open_file(filename):
    with open(filename) as file:
        sudoku = []
        while True:
            line = file.readline()
            if not line:
                break
            if line[0] != 'G' and len(sudoku) < 9:
                sudoku.append(list(line.strip('\n')))
            if len(sudoku) == 9:
                sudoku = [[int(j) for j in i] for i in sudoku] # convert from str to int
                yield sudoku
                sudoku = []

start = time.time()

endsum = 0
for grid in open_file('problem96.txt'):
    solve(grid)

print(f'The end sum of all top-left three digit numbers is {endsum}')
print(f'Program ran for {time.time()-start:.3f} seconds')
