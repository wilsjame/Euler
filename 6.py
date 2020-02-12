# The sum of the square of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the sqaures of the first
# ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first
# hundred natural numbers and the square of the sum.

def main():
	n = 100
	print(squareSum(n) - sumSquare(n))

def sumSquare(n):
	s = 0
	for i in range(1, n + 1):
		s += i * i

	return s

def squareSum(n):
	s = 0
	for i in range(1, n + 1):
		s += i

	return s * s

main()
