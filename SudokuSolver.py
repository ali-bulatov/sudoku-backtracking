#!/usr/bin/env python

def find_next_empty(puzzle):
    """Finds the next row,col on the puzzle that's not filled yet - represented as -1
    Return row, col tuple or (None,None) if there is none"""

    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col

    # Return None,None if there is no empty space left
    return None, None

def is_valid(puzzle, guess, row, col):
    """"Check if the guess at row/col is valid.
    Returns True of False"""

    # For a guess to be valid the number must not appear in the row/col/3x3 matrix

    # First check the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # Next check the colums
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # Check the square matrix
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for row in range(row_start, row_start + 3):
        for col in range(col_start, col_start + 3):
            if puzzle[row][col] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    """Solve the given Sudoku puzzle using backtracking.
    A puzzle is represented as a list of lists, where
    each inner list is a row in a Sudoku Puzzle.
    Returns True if the solution exists.
    Mutates the puzzle to be the solution (if exists)"""

    # step 1: choose some place in the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there's nowehre left, then we're done because we only allowed valid inputs
    if row == None:
        return True

    # step 2: if there is a place to put a new number in, then a make a guess from 1 to 9
    for guess in range(1,10):
        # step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
            puzzle[row][col] = guess
            # step 4: recursively call the solver with the new data
            if solve_sudoku(puzzle):
                return True
        # step 5: if not valid or if nothing gets returned true, then we need to backtrack and try a new number
        puzzle[row][col] = -1

    # step 6: if none of the numbers that we try work, then the puzzle is unsolvable
    return False

if __name__ == '__main__':
    test_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(test_board))
    for i in range(9):
        print(test_board[i])
