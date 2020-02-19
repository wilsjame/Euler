# Power digit sum
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number 2^1000?

def main():
	n = 2**1000
	sum = 0
	for x in str(n):
		sum += int(x)
	print(sum)
	
main()
