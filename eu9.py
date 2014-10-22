# Project Euler #9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# This runs super slow, but it gets the job done. 
# I am not sure how many squares I need to do the triplet checks.
# Clearly I don't need 999^2, but I am not sure where to cut it off logically. 

def squares():
	squares = []
	for i in range(1, 999):
		squares.append(i ** 2)
	return squares

def pythagtrip():
	squ = squares()
	trip = []
	for x in squ:
		for y in squ:
			if x + y in squ:
				trip.append(x)
				trip.append(y)
				trip.append(x + y)
	return trip

def sumthou():
	triplet = pythagtrip()
	while len(triplet) > 0:
		c = triplet.pop() ** 0.5
		b = triplet.pop() ** 0.5
		a = triplet.pop() ** 0.5
		if a + b + c == 1000:
			break
	print a * b * c

sumthou()

# The answer is 31875000
