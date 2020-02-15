# useful functions
import math

def isPrime(n):
	if n == 1:
		return False
	# 2 and 3 are prime
	elif n < 4:
		return True
	# evens 
	elif n % 2 == 0:
		return False
	# 5 and 7 are prime
	elif n < 9:
		return True
	elif n % 3 == 0:
		return False
	else:
		# round to the greatest int r so r*r<=n
		r = math.floor(math.sqrt(n))
		f = 5
		# all primes > 3 can be written as 6k +/- 1
		while f <= r:
			if n % f == 0: #6k-1
				return False
			if n % (f + 2) == 0: #6k+1
				return False
			f = f + 6 #6k
		return True

def nthPrime(n):
	candidate = 1
	count = 1 # know 2 is prime
	while count < n:
		candidate = candidate + 2 # skip evens
		if isPrime(candidate):
			count += 1
	return candidate
