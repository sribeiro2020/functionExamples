# Simulate a coin flip

import random

def flip(): #  No arguments here (important)
	"""
	Simulates a fair coin flip. Returns either "heads" or "tails".
	"""
	
	if random.random () <.5:
		return "heads"
	else:
		return "tails"
		
	
headsOrTails = flip()

print("The coin is {}.".format(headsOrTails))