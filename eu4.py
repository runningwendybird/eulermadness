# Find the largest palindrome made from the product of two 3-digit numbers.
#
def pal3():
	pal = []
	for n in range(100, 1000):
		for p in range(100, 1000):
			q = n * p
			q = str(q)
			r = list(q)
			if len(r) == 6 and r[0] == r[-1] and r[1] == r[-2] and r[2] == r[-3] and r[0] == "9":
				r = ''.join(r)
				pal.append(r)
	print pal

pal3()

# The answer is 906609
