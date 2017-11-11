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
	time.sleep(3)

# def solve(board):
# 	for row in board:
# 		options = np.setdiff1d(possibilities, row)
# 		print(row)
# 		print(options)
# 		for column in range(board):
# 			options = np.setdiff1d(options, board[:column])
# 			# print(column)
# 			print(options)
# 		options  = np.array([])

def solve(board):
	dimension = len(board[0])

	for row in range(dimension):
		row_options = np.setdiff1d(possibilities, board[row])
		# print(board[row])
		# print(row_options)
		for column in range(dimension):
			column_options = np.setdiff1d(possibilities, board[:, column])
			options = np.intersect1d(row_options, column_options)
			# print(board[:, column])
			# print(column_options)
			# print(options)

			if (board[row ,column] == 0):
				board[row, column] = options[0]
				print_sudoku(board)




			options = np.array([])
			# print(options)
			# print('----------------')


if __name__ == "__main__":
   grid = np.loadtxt(sys.argv[1]).astype(int)
   print_sudoku(grid)
   solve(grid)
