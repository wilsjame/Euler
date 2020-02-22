# Factorial digit sum
# 10! = 3628800
# The sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!1: unknown file attribute:  

def main():
	n = 100
	f = factorial(n)
	sum = 0
	for x in str(f):
		sum += int(x)
	print(sum)

def factorial(n):
	fact = n
	while n > 1:
		n -= 1
		fact *= n
	return fact

main()
