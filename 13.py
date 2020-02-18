# Large sum
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

def main():

	# get the 150-digit number
	with open('13.txt', 'r') as f:
		read_data = f.readlines()

	l = []
	for line in read_data:
		line = line.strip()
		l.append(line)

	# brute force
	sum = 0
	for x in l:
		sum += int(x)

	print(sum)

main()
