# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

def fib():
	n = 1
	m = 2
	sum = 2
	while n <= 4000000:
		p = n + m
		if p % 2 == 0:
			sum = sum + p
		n = m
		m = p
	print sum

fib()

# The answer is 4613732