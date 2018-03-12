# Text - Check if Palindrome

"""
1) Takes user input.
2) Check if input is palindrome.
3) Return result.
"""

# Imports
import subprocess

# Function - Clears screen
def cls():
	subprocess.call("cls", shell = True)
	
# Code start
programLoop = True
while programLoop == True:
	cls()
	# Checks if input is valid. Alphabetic characters only.
	inputLoop = True
	while inputLoop == True:
		cls()
		print "Text - Check if palindrome"
		userInput = raw_input("Please provide an input: ")
		if userInput.isalpha() == False:
			print "Please input one word only, limited to letters from the English alphabet."
			raw_input()
		else:
			inputLoop = False

	# Calculates maximum number of characters in provided string.
	# Minus one because counting starts from zero.
	inputLength = int(len(userInput)-1)
	# Calculates half of total length, to know where to stop checking loop.
	inputHalf = (inputLength+1)//2
	inputList = list(userInput)

	for i in range(0,inputHalf):
		# 0, 8-0 | 1, 8-1 | 2, 8-2
		if inputList[i] != inputList[(inputLength-i)]:
			raw_input("\nThe provided word is not a palindrome.")
			break
		elif i == (inputHalf-1):
			raw_input("\nThe provided word is a palindrome.")