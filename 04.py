# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 * 99
#
# Find the largest palindrome made from the product of two 3-digit numbers.
import math

def main():
	# [100, 999]
	a = range(100, 1000) 
	b = range(100, 1000)
	largestPalindrome = 0

	for i in a:
		for j in b:
			if palindrome(i * j) and i * j > largestPalindrome: 
				largestPalindrome = i * j

	print(largestPalindrome)
	
	return 0
	
def palindrome(n):
	s = str(n)
	digits = []
	palindrome = True

	for d in s:
		digits.append(int(d))
	
	# even number of digits in n
	if len(digits) % 2 == 0:
		# compare digits from the outside in --> <--
		for i in range(int(len(digits) / 2)):
			if digits[i] != digits[len(digits) - 1 - i]:
				palindrome = False

	# odd
	else:
		# --> <--
		for i in range(math.ceil(len(digits) / 2)):
			if digits[i] != digits[len(digits) - 1 - i]:
				palindrome = False
		
	return palindrome

main()
