# Numbers - Sieve of Eratosthenes

"""
1) Accept user input up to 1 million.
2) Enumerate everything from 1 to user input.
3) Iterate through and find multiples of 2.
4) Repeat (2) with 3.
5) Sieve the remaining numbers.
"""

# Imports
import subprocess

# Function - Clears screen
def cls():
	subprocess.call("cls", shell = True)

programLooping = True
while programLooping == True:
	# Checks that input is positive integers only.
	inputLoop = True
	while inputLoop == True:
		cls()
		print "Numbers - Sieve of Eratosthenes"
		try:
			userInput = int(raw_input("\nPlease provide an upper limit: "))
		except ValueError:
			raw_input("Please enter positive integers only!")
		else:
			if userInput <= 1:
				raw_input("Please enter positive integers only!")
			else:
				inputLoop = False

	# Adds every number from 1 to userInput to a list
	inputList = []
	for i in range(1, userInput+1):
		inputList.append(i)	
	# New list var, will contain prime numbers from inputList.
	primeList = []
	# Loops the sieve while inputList still has elements.
	# Moves 1 over before sieving.
	primeList.append(inputList.pop(0))
	x = 0
	y = 1
	while inputList != []:
		# Start sieving. Uses 2 to remove multiples of itself from inputList.
		primeList.append(inputList.pop(0))
		if inputList != []:
			# !!! Issue with next line - When the last number of the list is being checked, it skips the entire code block because
			# the condition evaluates to being True.
			toCompare = len(inputList)
			while toCompare != 0:
				if inputList[x] % primeList[y] == 0:
					del inputList[x]
					toCompare -= 1
				else:
					x += 1
					toCompare -= 1
		x = 0
		y += 1
		
	print "\nFor numbers from 1 to {0}, there are {1} prime numbers.".format(userInput, len(primeList))
	raw_input("The prime numbers are {0}".format(primeList))