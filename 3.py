# The prime factors of 13195 are 5, 7, 13 and 29
# What is the largest prime factor of the number 600851475143? 
# thx to xisk on math.stackexhange

def main():
	a = 600851475143
	#a = 13195

	# current divisor store
	b = 2

	# largest divisor store
	c = None

	while True:
		if a % b == 0:
			a = a / b
			c = b
			if a == 1:
				break;
		else:
			b += 1

	print(c)
		
main()
