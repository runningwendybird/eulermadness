# This is Euler Project's 6th problem
# Sum Square Difference
# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.

def sum_square():
	"""This will calculate the sum of the squares for the first 100 natural numbers"""
	sum = 0
	for i in range(1, 101):
		sum += i ** 2
	return sum

def square_sum():
	"""This will calculate the square of the sum of the first 100 natural numbers"""
	ssum = 0
	for n in range(1, 101):
		ssum += n
	square = ssum ** 2
	return square
	
def sub():
	sum = sum_square()
	square = square_sum()
	print square - sum

sub()

# The answer is 25164150
