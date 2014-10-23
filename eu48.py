# Project Euler #48
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

def self_powers():
	max_n = 1000
	sum = 0
	for n in range(1, max_n + 1):
		sum += n ** n
	final_digits = []
	n_string =list(str(sum))
	i = 1
	while i <= 10:
		final_digits.append(n_string.pop())
		i += 1
	final_digits.reverse()
	return final_digits

print self_powers()
