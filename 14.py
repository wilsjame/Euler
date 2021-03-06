# Longest Collatz sequence
# The following iterative sequence is defined for the set of positive integers:
# 
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# # Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.

def main():
	chain = 0
	num = None
	for i in range(1,1000000):
		if hailstorm(i) > chain:
			chain = hailstorm(i)
			num = i
	print(num)
	print(chain)

	return 0
	
# returns chain length from n --> 1
# Collatz problem
# use memoization for efficiency
memo = {}
def hailstorm(n):
	if n == 1:
		return 1
	if n in memo:
		return memo[n]
	if n % 2 == 0:
		memo[int(n)] = 1 + hailstorm(n / 2)
	else: # odd
		memo[int(n)] = 2 + hailstorm((3 * n + 1) / 2)

	return memo[n]

main()
