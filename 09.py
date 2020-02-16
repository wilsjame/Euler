# Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c,
# for which a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def main():
	l = [1, 4, 9]
	search = True

	# brute force *sigh*
	while search:
		print(l)
		for i in range(0, len(l) - 2):
			print("l[i] = " + str(l[i]))
			for j in range(i + 1, len(l) - 1):
				print("l[j] = " + str(l[j]))
				if l[i] + l[j] == l[len(l) - 1]:
					if (i + 1) + (j + 1) + (len(l)) == 1000:
						a = i + 1
						b = j + 1
						c = len(l)
						search = False
		l.append((len(l) + 1) * (len(l) + 1))

	print(str(l[i]) + " + " + str(l[j]) + " = " + str(l[len(l) - 1]))
	print("a = " + str(a))
	print("b = " + str(b))
	print("c = " + str(c))
	print("abc = " + str(a * b * c))

	return 0
					
main()
