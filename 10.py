# Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
import math

# set method from rosetta code
def eratosthenes2(n):
	#sum = 0
	multiples = set()
	for i in range(2, n + 1):
		if i not in multiples:
			#sum += i
			#print(sum)
			multiples.update(range(i * i, n + 1, i))
#eratosthenes2(10)

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

# sum of primes below limit
sum = 0
limit = 2000000
sieve = (eratosthenes(limit))
for n in range(2, limit):
	if sieve[n] == False:
		sum = sum + n
print(sum)
