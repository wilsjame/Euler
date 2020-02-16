# 2520 is the smallest number than can be divided by each of the numbers
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisble by all of
# the numbers from 1 to 20?

def main():
	n = 1
	while divisible(n) == False:
		n += 1

	print(n)

	return 0

def divisible(n):
	for i in range(1, 21): # [1, 20]
		if n % i != 0:
			return False
	
	return True

main()
