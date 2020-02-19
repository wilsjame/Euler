# Lattice paths
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# 
# How many such routes are there through a 20×20 grid?
def main():
	# combinatorial solution
	# count routes
	# 40 choose 20
	routes = factorial(40) / (factorial(20) * factorial(40 - 20))
	return routes

def factorial(n):
	factorial = 1
	for i in range(1, n + 1):
		factorial *= i

	return factorial

print(main())
