# Amicable numbers
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# 
# Evaluate the sum of all the amicable numbers under 10000.

# returns the sum of proper divisors of n
# (numbers less than n which divide evenly in to n)
def d(n):
	sum = 0
	for i in range(1, n):
		if n % i == 0:
			sum += i
	return sum

# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an 
# amicable pair and each of a and b are called amicable numbers.
def amicable(a):
	b = d(a)
	if d(b) == a and a != b:
		print(str(a) + " and " + str(b) + " are amicable")
		return True
	else:
		return False

def main():
	sum = 0
	i = 1
	while i < 10000:
		if amicable(i) == True:
			sum += (i + d(i))
		i += 1
	
	# halve the value as both pairs
	# are included in the sum
	print(sum/2)

	return 0

main()
