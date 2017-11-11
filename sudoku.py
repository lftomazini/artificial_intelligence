import sys
import os
import numpy as np
import math
import time

possibilities = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

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


def assigned_in_row(board, row, option):
	row_options = np.setdiff1d(possibilities, board[row])
	# print(row_options)
	if (option in row_options):
		# print(str(option) + " was already used in row " + str(row))
		return True
	else:
		# print(str(option) + " was NOT used in row " + str(row))
		return False

def assigned_in_column(board, column, option):
	column_options = np.setdiff1d(possibilities, board[:, column])
	# print(column_options)
	if (option in column_options):
		# print(str(option) + " was already used in column " + str(column))
		return True
	else:
		# print(str(option) + " was NOT used in column " + str(column))
		return False

def assigned_in_grid(board, row, column, option):
	dimension = len(board[0])
	row = row // 3 * 3
	column = column // 3 * 3

	grid = board[row: row + 3, column: column + 3]
	# print(grid)
	grid = np.reshape(grid, dimension)
	grid_options = np.setdiff1d(possibilities, grid)
	# print(grid_options)

	if (option in grid_options):
		return True
	else:
		return False

def safe_position(board, row, column, option):
	return assigned_in_row(board, row, option) and assigned_in_column(board, column, option) and assigned_in_grid(board, row, column, option)

def solve(board):
	dimension = len(board[0])

	for row in range(dimension):
		for column in range(dimension):
			for option in range (1, 10):
				if (board[row ,column] == 0):
					if (safe_position(board, row, column, option)):
						board[row, column] = option
						print_sudoku(board)


if __name__ == "__main__":
   board = np.loadtxt(sys.argv[1]).astype(int)
   print_sudoku(board)
   solve(board)
