# The four adjacent digits in the 1000-digit number that have the greatest
# product are 9 * 9 * 8 * 9 = 5832.
# 
# 8.txt
#
# Find the thirteen adjacent digits in the 1000-digit number that have the
# greatest product. What is the value of this product?

def main():
	# get the 1000-digit number
	with open('08.txt', 'r') as f:
		read_data = f.read()

	l = []
	for x in read_data:
		if x != '\n':
			l.append(x)
	

	greatest_product = 0
	greatest_product_adjacent_digits = []
	adjacent = 13

	for i in range(0, len(l) - adjacent + 1):
		adjacent_digits = []
		product = 1
		for j in range(i, i + adjacent):
			adjacent_digits.append(l[j])
		for k in adjacent_digits:
			product *= int(k)
		if product > greatest_product:
			greatest_product = product
			greatest_product_adjacent_digits = adjacent_digits
			
	print(greatest_product_adjacent_digits) 
	print(greatest_product)

	return 0

main()
