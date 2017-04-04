# Assume we have a function called double. 
def double(number):
	"""

	Takes in a number, doubles it, and returns the doubled number.
	"""

	number *= 2

	return number 


# ---------- Main program below -------
original = input("Tell me a number. ")
original = int(original)

answer = double(original)

print("The answer is {} .".format(answer))