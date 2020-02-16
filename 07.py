# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
#
# What is the 10001st prime number?
import math

def main():
	nth_prime(10001)
	
	return 0

# returns primality of n (brute force)
def prime(n):
	for i in range(2, n):
		if n % i == 0:
			return False

	return True
	
def nth_prime(x):
	num = 3
	primes_calculated = 2

	# only even prime is 2
	if x == 1:
		return 2

	while primes_calculated < x:
		# skip even numbers
		num +=2
		if prime(num):
			primes_calculated += 1
			print(str(primes_calculated) + "th prime = " + str(num))
	return num

main()
