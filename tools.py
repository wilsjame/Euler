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

# returns a bool list from [2, N] where False indices are prime
def eratosthenes(N):
	limit = N
	crosslimit = math.floor(math.sqrt(limit))
	sieve = [False for i in range(0, limit)]
	sieve[0] = None
	sieve[1] = None
	# mark even numbers > 2 true
	n = 4
	while n < limit:
		sieve[n] = True
		n += 2
	n = 3
	while n <= crosslimit:
		if sieve[n] == False: # not marked, hence prime
			m = n * n
			while m < limit:
				sieve[m] = True
				m += 2 * n 
		n += 2
	return sieve

# sum of primes below N
# ex) N = 10 : 2+3+5+7 = 17
def sumPrimes(N):
	sum = 0
	limit = N
	sieve = (eratosthenes(limit))
	for n in range(2, limit):
		if sieve[n] == False:
			sum = sum + n
	return sum
