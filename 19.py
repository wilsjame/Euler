# Counting Sundays
# You are given the following information, but you may prefer to do some research for yourself.
# 
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
import calendar

def main():
	y = 1901
	m = 1
	d = 1
	count = 0

	# cycle through each day up until 12/31/2000
	while y <= 2000 and m <= 12 and d <= 31:
		print(str(y) + " " + str(m) + " " + str(d))
		if m == 2:
			if y % 4 == 0:
				if d == 29:
					d = 1
					m += 1
				else:
					d += 1
			elif d == 28:
				d = 1
				m += 1
			else:
				d += 1
		elif m == 9 or m == 4 or m == 6 or m == 11:
			if d == 30:
				d = 1
				m += 1
			else:
				d += 1
		elif d == 31:
			if m == 12:
				d = 1
				m = 1
				y += 1
			else:
				d = 1
				m += 1
		else:
			d += 1

		# check for sundays on the first of the month
		if d == 1 and calendar.weekday(y, m, d) == 6:
			count += 1
		
	print(count)

main()
