import sys
import os
import numpy as np
import math
import time

# Possible numbers to put
possibilities = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Used to backtrack, appends a tuple containing the coordinates and the number put
filled = []

# Used to bactrack in a guided search
heuristic_array = []

# Prints the sudoku board
def print_sudoku(board):
    os.system('clear')
    print("-"*37)
    for i, row in enumerate(board):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i == 8:
            print("-"*37)
        elif i % 3 == 2:
            print("|" + "---+"*8 + "---|")
        else:
            print("|" + "   +"*8 + "   |")
    time.sleep(1)


# Verifies if a given number was put in a board row
def assigned_in_row(board, row, option):
    row_options = np.setdiff1d(possibilities, board[row])
    if (option in row_options):
        return True
    else:
        return False


# Verifies if a given number was put in a board column
def assigned_in_column(board, column, option):
    column_options = np.setdiff1d(possibilities, board[:, column])
    if (option in column_options):
        return True
    else:
        return False


# Verifies if a given number was put in a board grid
def assigned_in_grid(board, row, column, option):
    dimension = len(board[0])
    row = row // 3 * 3
    column = column // 3 * 3

    grid = board[row: row + 3, column: column + 3]
    grid = np.reshape(grid, dimension)
    grid_options = np.setdiff1d(possibilities, grid)

    if (option in grid_options):
        return True
    else:
        return False


# Verifies if a number wasn't put in neither a row, column or grid
def safe_position(board, row, column, option):
    return assigned_in_row(board, row, option) and assigned_in_column(board, column, option) and assigned_in_grid(board, row, column, option)


# Solves the sudoku board, backtracking when it gets stuck
def solve(board):
    dimension = len(board[0])
    row = 0
    column = 0
    option = 1

    while (row < dimension):
        while (column < dimension):
            if (board[row ,column] == 0):
                while (option <=  10):
                    if (safe_position(board, row, column, option)):
                        board[row, column] = option
                        filled.append([row, column, option])
                        print_sudoku(board)
                        break
                    option += 1
                if (option == 11):
                    row = filled[-1][0]
                    column = filled[-1][1] - 1
                    option = filled[-1][2] + 1
                    board[row, column + 1] = 0
                    print_sudoku(board)
                    del filled[-1]
                else:
                    option = 1
            column += 1
        column = 0
        row += 1

'''
Guided Search
A-Star algorithm to solve Sudoku
Reference: https://github.com/SAURABHMARATHE/a-star_algorithm_code_for_sudoku/blob/master/my_a_star_for_sudoku.py
'''

# Calculate the heuristic associated with each cell
def heuristic (board):
    # Array to store the possible values for each cell


    bestRow = 0
    bestColumn = 0
    dimension = len(board[0])

    for row in range (0, dimension):
        for column in range (0, dimension):
            if (board[row, column] == 0):
                possible_values = []
                for option in range(1, 10):
                    if (safe_position(board, row, column, option)):
                        possible_values.append(option)

                # Heuristic is the length of possible_values. The shorter is the array, the better is the heuristic.
                heuristic_array.append([row, column, len(possible_values)])

    # Calculate the cost of heuristic and takes the best position for the board.
    dimension  = len(possible_values)
    bestRow = heuristic_array[row][0]
    bestColumn = heuristic_array[row][1]
    minimum = heuristic_array[0][2]

    # Search for the minimum heuristic (best first)
    for row in range(0, dimension):
        if(heuristic_array[row][2] < minimum):
            bestRow = heuristic_array[row][0]
            bestColumn = heuristic_array[row][1]
            minimum = heuristic_array[row][2]

    del heuristic_array[bestRow]

    return bestRow, bestColumn

# Solve the Sudoku board using the A Star Algorithm
def run_a_star (board):
    solved_cells = np.count_nonzero(board)
    # print(solved_cells)

    while (solved_cells < 81):
        row, column = heuristic(board)
        for option in range (1, 10):
            if (safe_position(board, row, column, option)):
                board[row, column] = option
                filled.append([row, column, option])
                print_sudoku(board)
                solved_cells += 1
                break

if __name__ == "__main__":
    board = np.loadtxt(sys.argv[2]).astype(int)

    if (str(sys.argv[1]) == "-i"):
        print_sudoku(board)
        run_a_star(board)
    elif (str(sys.argv[1]) == "-u"):
        print_sudoku(board)
        solve(board)
