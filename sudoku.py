import sys
import numpy as np
import math

def print_sudoku(board):
	print("-"*37)
	for i, row in enumerate(board):
		print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
		if i == 8:
			 print("-"*37)
		elif i % 3 == 2:
			print("|" + "---+"*8 + "---|")
		else:
			print("|" + "   +"*8 + "   |")

if __name__ == "__main__":
   grid = np.loadtxt(sys.argv[1]).astype(int)
   print_sudoku(grid)

