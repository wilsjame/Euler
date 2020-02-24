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
	# only even prime is 2
	if n == 1:
		return 2
		
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

# returns a dictionary of prime factors and their count 
# key = prime factor: value = count
# ex) 10 --> (2: 1, 5: 1)
def primeFactorization(n):
	i = 1 # prime iterator
	primeFactors = {}
	if isPrime(n): # input is prime off the bat
		primeFactors[n] = 1
	else:
		while n > 1 and isPrime(n) == False:
			while n % nthPrime(i) == 0: 
				if nthPrime(i) not in primeFactors:
					primeFactors[nthPrime(i)] = 1
				else:
					primeFactors[nthPrime(i)] = primeFactors[nthPrime(i)] + 1
				n = int(n / nthPrime(i))
			i += 1
		# n / nthPrime(i) > 1 when the last two prime factors are not the same 
		# ex) 10 --> [2,5]
		# which means n is a prime factor that still needs to be added the list
		if n > 1:
			primeFactors[n] = 1

	return primeFactors

# finds the sum of the maxmium total path taken from top 
# to bottom in a triangle. Uses the bottom up approach.
#arr = [
#[3],
#[7, 4],
#[2, 4, 6],
#[8, 5, 9, 3,]]
# result --> 23
def maxPathSumTriangle(arr):
	m = len(arr) - 2 # second to last row
	while m >= 0:
		for i in range(len(arr[m])):
			if arr[m+1][i] > arr[m+1][i+1]:
				arr[m][i] += arr[m+1][i]
			else:
				arr[m][i] += arr[m+1][i+1]
		m -= 1

	return arr[0]

# Greatest common divisor (GCD) or 
# highest common factor (HCF) is the 
# largest positive integer that divides 
# all the given numbers without giving a remainder.
#t1 = [2,4,6,8,10] # GCD = 2
#t2 = [2,3,4,5,6] # GCD = 1
#t3 = [36,72] # GCD = 36
def gcd(nums):
	#TODO sort the numbers from low to high
	prime_factors = []
	gcd = 1
	# find the prime factors for each number
	for n in nums:
		prime_factors.append(primeFactorization(n))
	# compare the prime factors of the first (smallest) number with the other numbers,
	# and determine if it is a shared divisor
	for k in prime_factors[0]:
		shared_div = True
		count = 0
		while count < prime_factors[0][k]:
			for d in range(len(prime_factors)):
				if d == 0: # these are the prime factors of the smallest number we're comparing to
					None
				else:
					if k not in prime_factors[d]:
						shared_div = False
			# keep a running product of all the shared divisors,
			# this will be the GCD
			if shared_div == True:
				gcd *= k
			count += 1

	return gcd
