# The prime factors of 13195 are 5, 7, 13 and 29
# What is the largest prime factor of the number 600851475143? 

def main():
	#n = 600851475143
	n = 13195
	pl = []

	pl = primes(n)

	# prime factors
	for p in pl:
		if n % p == 0:
			print(p)

	return

# returns a list of prime numbers in the range [2,n]
def primes(n):
	l = list(range(0, n+1))
	primes = []
	p = 1
	stop = False

	# find first number greater than p and mark as prime
	while stop == False:
		stop = True
		for x in range(len(l)):
			if l[x] > p:
				p = l[x]
				stop = False
				break;

		# mark composites
		i = 2
		while i * p <= n:
			l[i * p] = 0
			i += 1
		
	# clean out l
	del l[1]

	# primes
	for p in l:
		if p != 0:
			primes.append(p)

	return primes

main()
