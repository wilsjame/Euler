# Largest product in a grid
# In the 20 x 20 grid (11.txt), four numbers along a diagonal 
# line have been marked in red. The product of these numbers 
# is 26 * 63 * 78 * 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the 
# same direction (up, down, left, right, or diagonally) in the
# 20 x 20 grid?

def main():
	N = 20 # N X N grid size
	adj = 4 # adjacent numbers to multiply
	# get the grid
	rows, cols = N, N
	grid = [[0 for i in range(cols)] for j in range(rows)]
	with open('11.txt', 'r') as f:
		row = 0
		for line in f:
			line = line.strip()
			line = line.split(' ')
			for col in range(len(line)):
				grid[row][col] = int(line[col])
			row += 1	

		print(leftRight(grid, N, adj))
		print(upDown(grid, N, adj))
		print(diagonal(grid, N, adj))
			
def leftRight(g, N, adj):
	max_product = 0
	for x in range(N):
		for y in range(0, N - adj + 1):
			product = g[x][y]*g[x][y+1]*g[x][y+2]*g[x][y+3]
			if product > max_product:
				max_product = product

	return max_product

def upDown(g, N, adj):
	max_product = 0
	for y in range(N):
		for x in range(0, N - adj + 1):
			product = g[x][y]*g[x+1][y]*g[x+2][y]*g[x+3][y]
			if product > max_product:
				max_product = product

	return max_product

# includes both \ and / diagonals
def diagonal(g, N, adj):
	max_product = 0
	# \ diagonal
	for x in range(0, N - adj + 1):
		for y in range(0, N - adj + 1):
			p = g[x][y]*g[x+1][y+1]*g[x+2][y+2]*g[x+3][y+3]
			if p > max_product:
				max_product = p

	# / diagonal
	for x in range(0, N - adj + 1):
		for y in range(adj - 1, N):
			p = g[x][y]*g[x+1][y-1]*g[x+2][y-2]*g[x+3][y-3]
			if p > max_product:
				max_product = p

	return max_product

main()
