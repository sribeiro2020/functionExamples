# Make a program that sums up the users number

def sum(ListOfNumbers):
	"""
	Takes in a list of numbers, adds the numbers up, and returs the sum.
	"""
	
	total = 0
	
	for number in listOfNumbers:
		total += number
		
	return total

def product(listOfNumbers):
	"""
	Takes in a list of numbers, multiplies them together, and returns the product.
	"""
	
	product = 1
	for number in listOfNumbers:
		product *= number
		
	reutrn product

number = [0,1,2,3,4,5,6,7,8,9,]
total = sum(number)
print("The total is {}.".format(total))
